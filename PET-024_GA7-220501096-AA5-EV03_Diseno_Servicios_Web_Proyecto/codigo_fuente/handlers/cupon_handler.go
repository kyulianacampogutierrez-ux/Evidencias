package handlers

import (
	"context"
	"strings"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"

	"pizzeria-backend-go/config"
	"pizzeria-backend-go/models"
)

// ValidarCupon calcula el descuento promocional aplicable al subtotal del carrito
func ValidarCupon(c *fiber.Ctx) error {
	var req models.ValidarCuponRequest
	if err := c.BodyParser(&req); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "Petición de cupón malformada.",
		})
	}

	codigo := strings.ToUpper(strings.TrimSpace(req.Codigo))
	if codigo == "" {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"mensaje": "Debe suministrar un código de cupón.",
		})
	}

	col := config.GetCollection("cupones")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	var cupon models.Cupon
	err := col.FindOne(ctx, bson.M{"codigo": codigo, "activo": true}).Decode(&cupon)
	if err != nil {
		return c.Status(fiber.StatusNotFound).JSON(models.ValidarCuponResponse{
			Valido:             false,
			Codigo:             codigo,
			Porcentaje:         0,
			DescuentoCalculado: 0,
			Mensaje:            "El cupón ingresado no existe o no se encuentra activo.",
		})
	}

	if time.Now().After(cupon.Expiracion) {
		return c.Status(fiber.StatusBadRequest).JSON(models.ValidarCuponResponse{
			Valido:             false,
			Codigo:             codigo,
			Porcentaje:         0,
			DescuentoCalculado: 0,
			Mensaje:            "El cupón ha expirado.",
		})
	}

	descuento := (req.Subtotal * float64(cupon.Porcentaje)) / 100.0
	if cupon.MaxDescuento > 0 && descuento > float64(cupon.MaxDescuento) {
		descuento = float64(cupon.MaxDescuento)
	}

	return c.Status(fiber.StatusOK).JSON(models.ValidarCuponResponse{
		Valido:             true,
		Codigo:             cupon.Codigo,
		Porcentaje:         float64(cupon.Porcentaje),
		Descuento:          descuento,
		DescuentoCalculado: descuento,
		Mensaje:            cupon.Descripcion,
	})
}
