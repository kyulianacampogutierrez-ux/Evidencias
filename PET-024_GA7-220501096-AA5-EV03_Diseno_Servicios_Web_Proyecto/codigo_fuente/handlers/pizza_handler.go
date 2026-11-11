package handlers

import (
	"context"
	"strings"
	"time"

	"github.com/gofiber/fiber/v2"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo/options"

	"pizzeria-backend-go/config"
	"pizzeria-backend-go/models"
)

// GetCategorias retorna las categorías de la carta de la pizzería
func GetCategorias(c *fiber.Ctx) error {
	col := config.GetCollection("categorias")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	cursor, err := col.Find(ctx, bson.M{"activa": true})
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"error":   "INTERNAL_ERROR",
			"mensaje": "Error al consultar las categorías en MongoDB.",
		})
	}
	defer cursor.Close(ctx)

	var categorias []models.Categoria
	if err := cursor.All(ctx, &categorias); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al decodificar categorías.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success":    true,
		"total":      len(categorias),
		"categorias": categorias,
	})
}

// GetPizzas retorna el catálogo completo de pizzas con filtros opcionales
func GetPizzas(c *fiber.Ctx) error {
	categoria := c.Query("categoria")
	busqueda := c.Query("q")
	soloDestacadas := c.Query("destacadas") == "true"

	filter := bson.M{}
	if categoria != "" {
		filter["categoria"] = strings.ToUpper(categoria)
	}
	if soloDestacadas {
		filter["destacada"] = true
	}
	if busqueda != "" {
		filter["$or"] = []bson.M{
			{"nombre": bson.M{"$regex": busqueda, "$options": "i"}},
			{"descripcion": bson.M{"$regex": busqueda, "$options": "i"}},
		}
	}

	col := config.GetCollection("pizzas")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	opts := options.Find().SetSort(bson.D{{Key: "destacada", Value: -1}, {Key: "nombre", Value: 1}})
	cursor, err := col.Find(ctx, filter, opts)
	if err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"error":   "INTERNAL_ERROR",
			"mensaje": "Error al consultar las pizzas en MongoDB.",
		})
	}
	defer cursor.Close(ctx)

	var pizzas []models.Pizza
	if err := cursor.All(ctx, &pizzas); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al decodificar pizzas.",
		})
	}

	if c.Query("wrapper") == "true" {
		return c.Status(fiber.StatusOK).JSON(fiber.Map{
			"success": true,
			"total":   len(pizzas),
			"pizzas":  pizzas,
		})
	}
	return c.Status(fiber.StatusOK).JSON(pizzas)
}

// GetPizzaByCodigo retorna una pizza específica por su código
func GetPizzaByCodigo(c *fiber.Ctx) error {
	codigo := c.Params("codigo")

	col := config.GetCollection("pizzas")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	var pizza models.Pizza
	err := col.FindOne(ctx, bson.M{"codigo": codigo}).Decode(&pizza)
	if err != nil {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"success": false,
			"error":   "NOT_FOUND",
			"mensaje": "Pizza no encontrada en la carta.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"pizza":   pizza,
	})
}

// CreatePizza permite a los administradores registrar una nueva pizza en la carta
func CreatePizza(c *fiber.Ctx) error {
	var pizza models.Pizza
	if err := c.BodyParser(&pizza); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "JSON inválido en el cuerpo de la petición.",
		})
	}

	if pizza.Codigo == "" || pizza.Nombre == "" || pizza.Precios.Mediana == 0 {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "El código, nombre y precio de la pizza son obligatorios.",
		})
	}

	col := config.GetCollection("pizzas")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	count, _ := col.CountDocuments(ctx, bson.M{"codigo": pizza.Codigo})
	if count > 0 {
		return c.Status(fiber.StatusConflict).JSON(fiber.Map{
			"success": false,
			"error":   "CONFLICT",
			"mensaje": "Ya existe una pizza registrada con este código.",
		})
	}

	pizza.Disponible = true
	if _, err := col.InsertOne(ctx, pizza); err != nil {
		return c.Status(fiber.StatusInternalServerError).JSON(fiber.Map{
			"success": false,
			"mensaje": "Error al guardar la nueva pizza en MongoDB.",
		})
	}

	return c.Status(fiber.StatusCreated).JSON(fiber.Map{
		"success": true,
		"mensaje": "Pizza agregada exitosamente a la carta",
		"pizza":   pizza,
	})
}

// UpdatePizza permite actualizar precios, ingredientes y disponibilidad
func UpdatePizza(c *fiber.Ctx) error {
	codigo := c.Params("codigo")

	var updates bson.M
	if err := c.BodyParser(&updates); err != nil {
		return c.Status(fiber.StatusBadRequest).JSON(fiber.Map{
			"success": false,
			"error":   "BAD_REQUEST",
			"mensaje": "Datos de actualización inválidos.",
		})
	}

	col := config.GetCollection("pizzas")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	result, err := col.UpdateOne(ctx, bson.M{"codigo": codigo}, bson.M{"$set": updates})
	if err != nil || result.MatchedCount == 0 {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"success": false,
			"error":   "NOT_FOUND",
			"mensaje": "Pizza no encontrada para actualizar.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"mensaje": "Pizza actualizada correctamente en la carta",
	})
}

// DeletePizza elimina un producto de la carta
func DeletePizza(c *fiber.Ctx) error {
	codigo := c.Params("codigo")

	col := config.GetCollection("pizzas")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	result, err := col.DeleteOne(ctx, bson.M{"codigo": codigo})
	if err != nil || result.DeletedCount == 0 {
		return c.Status(fiber.StatusNotFound).JSON(fiber.Map{
			"success": false,
			"error":   "NOT_FOUND",
			"mensaje": "Pizza no encontrada para eliminar.",
		})
	}

	return c.Status(fiber.StatusOK).JSON(fiber.Map{
		"success": true,
		"mensaje": "Pizza eliminada de la carta exitosamente.",
	})
}
