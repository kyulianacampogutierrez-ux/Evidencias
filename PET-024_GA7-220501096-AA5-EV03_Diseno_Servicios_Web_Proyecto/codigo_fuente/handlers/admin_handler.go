package handlers

import (
	"context"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"

	"pizzeria-backend-go/config"
	"pizzeria-backend-go/models"
)

// GetDashboardStats consolida las métricas comerciales y operativas para el Administrador
func GetDashboardStats(c *fiber.Ctx) error {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	pedidosCol := config.GetCollection("pedidos")
	pizzasCol := config.GetCollection("pizzas")
	usuariosCol := config.GetCollection("usuarios")

	totalPedidos, _ := pedidosCol.CountDocuments(ctx, bson.M{})
	pedidosPendientes, _ := pedidosCol.CountDocuments(ctx, bson.M{
		"estado": bson.M{"$in": []string{"RECIBIDO", "EN_PREPARACION", "EN_HORNO", "EN_CAMINO"}},
	})
	pedidosEntregados, _ := pedidosCol.CountDocuments(ctx, bson.M{"estado": "ENTREGADO"})
	totalPizzas, _ := pizzasCol.CountDocuments(ctx, bson.M{})
	totalUsuarios, _ := usuariosCol.CountDocuments(ctx, bson.M{})

	// Calcular ingresos totales sumando órdenes entregadas o pagadas
	cursor, err := pedidosCol.Find(ctx, bson.M{"estadoPago": "APROBADO"})
	ingresosTotales := 0
	if err == nil {
		var pedidos []models.Pedido
		if err := cursor.All(ctx, &pedidos); err == nil {
			for _, p := range pedidos {
				ingresosTotales += p.Total
			}
		}
		cursor.Close(ctx)
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success":           true,
		"totalVentas":       ingresosTotales,
		"pedidosActivos":    pedidosPendientes,
		"totalPedidos":      totalPedidos,
		"pedidosEntregados": pedidosEntregados,
		"metricas": fiber.Map{
			"totalVentas":         ingresosTotales,
			"totalVentasPesos":    ingresosTotales,
			"totalPedidos":        totalPedidos,
			"pedidosActivos":      pedidosPendientes,
			"pedidosEntregados":   pedidosEntregados,
			"catalogoPizzas":      totalPizzas,
			"clientesRegistrados": totalUsuarios,
		},
		"sucursal": "Sede Popayán - Centro Histórico",
		"aprendiz": "Karen Yuliana Campo - Ficha 228118",
	})
}

// ListarUsuarios retorna los clientes y administradores registrados
func ListarUsuarios(c *fiber.Ctx) error {
	col := config.GetCollection("usuarios")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	cursor, err := col.Find(ctx, bson.M{})
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al listar usuarios.",
		})
	}
	defer cursor.Close(ctx)

	var usuarios []models.Usuario
	if err := cursor.All(ctx, &usuarios); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al decodificar usuarios.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success":  true,
		"total":    len(usuarios),
		"usuarios": usuarios,
	})
}
