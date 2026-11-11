package handlers

import (
	"context"
	"fmt"
	"math/rand"
	"strings"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo/options"

	"pizzeria-backend-go/config"
	"pizzeria-backend-go/models"
)

// CrearPedido procesa el checkout del carrito y genera una nueva orden
func CrearPedido(c *fiber.Ctx) error {
	usuarioNombre, _ := c.Locals("usuario").(string)
	nombreCompleto, _ := c.Locals("nombre").(string)

	var req models.CrearPedidoRequest
	if err := c.BodyParser(&req); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "Cuerpo de orden inválido.",
		})
	}

	if len(req.Items) == 0 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "El carrito de compras no puede estar vacío.",
		})
	}

	if req.DireccionEntrega == "" && req.DireccionEnvio != "" {
		req.DireccionEntrega = req.DireccionEnvio
	}
	if req.CodigoCupon == "" && req.CuponCodigo != "" {
		req.CodigoCupon = req.CuponCodigo
	}
	if req.MedioPago == "" && req.MetodoPago != "" {
		req.MedioPago = req.MetodoPago
	}

	if strings.TrimSpace(req.DireccionEntrega) == "" {
		req.DireccionEntrega = "Popayán, Cauca"
	}

	// Calcular subtotal sumando items
	subtotal := 0
	for i := range req.Items {
		item := &req.Items[i]
		if item.Codigo == "" && item.PizzaCodigo != "" {
			item.Codigo = item.PizzaCodigo
		}
		if item.Nombre == "" {
			item.Nombre = "Pizza Bella Italia"
		}
		if item.Cantidad <= 0 {
			item.Cantidad = 1
		}
		if item.TotalItem <= 0 {
			item.TotalItem = item.PrecioUnitario * float64(item.Cantidad)
		}
		subtotal += int(item.TotalItem)
	}

	// Validar cupón si fue ingresado
	var descuentoCupon *models.DescuentoCupon
	descuentoValor := 0
	if req.CodigoCupon != "" {
		cuponCol := config.GetCollection("cupones")
		ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		var cupon models.Cupon
		err := cuponCol.FindOne(ctx, bson.M{
			"codigo": strings.ToUpper(strings.TrimSpace(req.CodigoCupon)),
			"activo": true,
		}).Decode(&cupon)
		cancel()

		if err == nil {
			calc := (subtotal * cupon.Porcentaje) / 100
			if cupon.MaxDescuento > 0 && calc > cupon.MaxDescuento {
				calc = cupon.MaxDescuento
			}
			descuentoValor = calc
			descuentoCupon = &models.DescuentoCupon{
				Codigo: cupon.Codigo,
				Valor:  descuentoValor,
			}
		}
	}

	costoEnvio := 4000
	if subtotal > 70000 {
		costoEnvio = 0 // Domicilio gratis por compras superiores a 70.000 COP
	}

	total := subtotal - descuentoValor + costoEnvio
	if total < 0 {
		total = 0
	}

	// Generar código de pedido legible: PED-2026-XXXX
	numRandom := rand.Intn(9000) + 1000
	numeroPedido := fmt.Sprintf("PED-2026-%04d", numRandom)

	medioPago := req.MedioPago
	if medioPago == "" {
		medioPago = "EFECTIVO"
	}

	estadoPago := "PENDIENTE"
	referencia := fmt.Sprintf("REF-%d", time.Now().Unix())
	if medioPago == "EFECTIVO" {
		estadoPago = "CONTRA_ENTREGA"
	}

	ahora := time.Now()
	nuevoPedido := models.Pedido{
		NumeroPedido:     numeroPedido,
		ClienteUsuario:   usuarioNombre,
		ClienteNombre:    nombreCompleto,
		ClienteTelefono:  "+57 312 000 0000",
		DireccionEntrega: req.DireccionEntrega,
		Items:            req.Items,
		Subtotal:         subtotal,
		DescuentoCupon:   descuentoCupon,
		CostoEnvio:       costoEnvio,
		Total:            total,
		MedioPago:        medioPago,
		EstadoPago:       estadoPago,
		ReferenciaPago:   referencia,
		Estado:           "RECIBIDO",
		HistorialEstados: []models.HistorialEstado{
			{
				Estado: "RECIBIDO",
				Fecha:  ahora,
				Nota:   "Pedido recibido en el sistema de Pizzería Bella Italia Popayán.",
			},
		},
		FechaCreacion:         ahora,
		TiempoEstimadoMinutos: 40,
	}

	col := config.GetCollection("pedidos")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if _, err := col.InsertOne(ctx, nuevoPedido); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"error":   "INTERNAL_ERROR",
			"mensaje": "Error al guardar el pedido en MongoDB.",
		})
	}

	return c.Status(fiber.StatusCreated).JSON(fiber.Map{
		"success": true,
		"mensaje": "¡Pedido realizado con éxito! En breve comenzará su preparación.",
		"pedido":  nuevoPedido,
	})
}

// GetMisPedidos retorna el historial de pedidos del cliente autenticado
func GetMisPedidos(c *fiber.Ctx) error {
	usuarioNombre, _ := c.Locals("usuario").(string)

	col := config.GetCollection("pedidos")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	opts := options.Find().SetSort(bson.D{{Key: "fechaCreacion", Value: -1}})
	cursor, err := col.Find(ctx, bson.M{"clienteUsuario": usuarioNombre}, opts)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al consultar los pedidos.",
		})
	}
	defer cursor.Close(ctx)

	var pedidos []models.Pedido
	if err := cursor.All(ctx, &pedidos); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al procesar la lista de pedidos.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"total":   len(pedidos),
		"pedidos": pedidos,
	})
}

// GetPedidoByNumero consulta el estado de un pedido para seguimiento en tiempo real
func GetPedidoByNumero(c *fiber.Ctx) error {
	numero := c.Params("numero")

	col := config.GetCollection("pedidos")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	var pedido models.Pedido
	err := col.FindOne(ctx, bson.M{"numeroPedido": numero}).Decode(&pedido)
	if err != nil {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"success": false,
			"error":   "NOT_FOUND",
			"mensaje": "Pedido no encontrado.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"pedido":  pedido,
	})
}

// GetTodosLosPedidos permite al administrador listar todos los pedidos con filtro de estado
func GetTodosLosPedidos(c *fiber.Ctx) error {
	estado := c.Query("estado")

	filter := bson.M{}
	if estado != "" {
		filter["estado"] = strings.ToUpper(estado)
	}

	col := config.GetCollection("pedidos")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	opts := options.Find().SetSort(bson.D{{Key: "fechaCreacion", Value: -1}})
	cursor, err := col.Find(ctx, filter, opts)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al consultar pedidos globales.",
		})
	}
	defer cursor.Close(ctx)

	var pedidos []models.Pedido
	if err := cursor.All(ctx, &pedidos); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al procesar la lista.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"total":   len(pedidos),
		"pedidos": pedidos,
	})
}

// ActualizarEstadoPedido permite al administrador avanzar el ciclo del pedido
func ActualizarEstadoPedido(c *fiber.Ctx) error {
	numero := c.Params("numero")

	var req models.ActualizarEstadoRequest
	if err := c.BodyParser(&req); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "Payload de estado inválido.",
		})
	}

	req.Estado = strings.ToUpper(strings.TrimSpace(req.Estado))
	estadosValidos := map[string]bool{
		"RECIBIDO":       true,
		"EN_PREPARACION": true,
		"EN_HORNO":       true,
		"EN_CAMINO":      true,
		"ENTREGADO":      true,
		"CANCELADO":      true,
	}

	if !estadosValidos[req.Estado] {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "INVALID_STATE",
			"mensaje": "Estado no válido. Opciones: RECIBIDO, EN_PREPARACION, EN_HORNO, EN_CAMINO, ENTREGADO, CANCELADO",
		})
	}

	nota := req.Nota
	if nota == "" {
		nota = fmt.Sprintf("Pedido pasó a estado: %s", req.Estado)
	}

	nuevoItemHistorial := models.HistorialEstado{
		Estado: req.Estado,
		Fecha:  time.Now(),
		Nota:   nota,
	}

	col := config.GetCollection("pedidos")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	update := bson.M{
		"$set": bson.M{
			"estado": req.Estado,
		},
		"$push": bson.M{
			"historialEstados": nuevoItemHistorial,
		},
	}

	result, err := col.UpdateOne(ctx, bson.M{"numeroPedido": numero}, update)
	if err != nil || result.MatchedCount == 0 {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"success": false,
			"error":   "NOT_FOUND",
			"mensaje": "Pedido no encontrado para actualizar estado.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success":      true,
		"mensaje":      fmt.Sprintf("Estado del pedido %s actualizado a %s", numero, req.Estado),
		"nuevoEstado":  req.Estado,
		"actualizado":  nuevoItemHistorial,
	})
}
