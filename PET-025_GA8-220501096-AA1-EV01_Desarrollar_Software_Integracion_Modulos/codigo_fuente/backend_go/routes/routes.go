package routes

import (
	"time"

	"github.com/gofiber/fiber/v2"
	"pizzeria-backend-go/handlers"
	"pizzeria-backend-go/middleware"
)

// SetupRoutes configura todos los endpoints de la API REST de la Pizzería Bella Italia
func SetupRoutes(app *fiber.App) {

	// 1. HEALTHCHECK & METADATOS DEL SISTEMA
	app.Get("/health", func(c *fiber.Ctx) error {
		return c.Status(fiber.StatusOK).JSON(fiber.Map{
			"status":    "UP",
			"servicio":  "pizzeria-backend-go-fiber",
			"database":  "MongoDB (pizzeria_db)",
			"version":   "2.0.0",
			"aprendiz":  "Karen Yuliana Campo",
			"ficha":     "228118",
			"centro":    "CTPI Popayán - Regional Cauca",
			"timestamp": time.Now().Format(time.RFC3339),
		})
	})

	api := app.Group("/api")
	api.Get("/health", func(c *fiber.Ctx) error {
		return c.Status(fiber.StatusOK).JSON(fiber.Map{
			"status":   "UP",
			"servicio": "pizzeria-backend-go-fiber",
			"database": "MongoDB (pizzeria_db)",
			"aprendiz": "Karen Yuliana Campo",
			"ficha":    "228118",
		})
	})

	// 2. MÓDULO DE AUTENTICACIÓN Y CLIENTES
	auth := api.Group("/auth")
	auth.Post("/register", handlers.Register)
	auth.Post("/login", handlers.Login)
	auth.Get("/profile", middleware.JWTMiddleware(), handlers.GetProfile)

	// 3. MÓDULO DE CARTA (CATÁLOGO DE PRODUCTOS)
	api.Get("/categorias", handlers.GetCategorias)
	api.Get("/pizzas", handlers.GetPizzas)
	api.Get("/pizzas/:codigo", handlers.GetPizzaByCodigo)

	// 4. MÓDULO DE CUPONES Y DESCUENTOS
	api.Post("/cupones/validar", handlers.ValidarCupon)

	// 5. MÓDULO DE PEDIDOS Y SEGUIMIENTO (TRACKING)
	pedidos := api.Group("/pedidos")
	pedidos.Get("/:numero", handlers.GetPedidoByNumero) // Seguimiento público con código de orden
	pedidos.Post("/", middleware.JWTMiddleware(), handlers.CrearPedido)
	pedidos.Get("/mis-pedidos", middleware.JWTMiddleware(), handlers.GetMisPedidos)

	// 6. MÓDULO DE MEDIOS DE PAGO
	pagos := api.Group("/pagos")
	pagos.Post("/procesar", handlers.ProcesarPago)

	// 7. MÓDULO DE ADMINISTRADOR (RESTRINGIDO CON ROL ADMIN)
	admin := api.Group("/admin", middleware.JWTMiddleware(), middleware.AdminOnlyMiddleware())
	admin.Get("/dashboard", handlers.GetDashboardStats)
	admin.Get("/pedidos", handlers.GetTodosLosPedidos)
	admin.Put("/pedidos/:numero/estado", handlers.ActualizarEstadoPedido)
	admin.Post("/pizzas", handlers.CreatePizza)
	admin.Put("/pizzas/:codigo", handlers.UpdatePizza)
	admin.Delete("/pizzas/:codigo", handlers.DeletePizza)
	admin.Get("/usuarios", handlers.ListarUsuarios)
}
