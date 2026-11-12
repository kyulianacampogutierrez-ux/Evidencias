package main

import (
	"log"
	"os"

	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"github.com/gofiber/fiber/v2/middleware/logger"
	"github.com/gofiber/fiber/v2/middleware/recover"

	"pizzeria-backend-go/config"
	"pizzeria-backend-go/routes"
)

func main() {
	// 1. Inicializar conexión con base de datos MongoDB
	config.ConnectDB()

	// 2. Crear instancia de aplicación Fiber v2
	app := fiber.New(fiber.Config{
		AppName:      "Pizzería Bella Italia - Backend REST API (Go + Fiber v2)",
		ServerHeader: "Fiber-Go",
	})

	// 3. Configurar Middlewares globales
	app.Use(recover.New())
	app.Use(logger.New(logger.Config{
		Format: "[${time}] ${status} - ${latency} ${method} ${path}\n",
	}))
	app.Use(cors.New(cors.Config{
		AllowOrigins: "*",
		AllowHeaders: "Origin, Content-Type, Accept, Authorization",
		AllowMethods: "GET, POST, HEAD, PUT, DELETE, PATCH, OPTIONS",
	}))

	// 4. Registrar Rutas de la API
	routes.SetupRoutes(app)

	// 5. Determinar puerto de escucha
	port := os.Getenv("PORT")
	if port == "" {
		port = "8085"
	}

	log.Printf("================================================================")
	log.Printf("SERVICIO REST: Pizzería Bella Italia (Go + Fiber v2 + MongoDB)")
	log.Printf("Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | ADSO CTPI Popayán")
	log.Printf("Servidor escuchando en: http://0.0.0.0:%s", port)
	log.Printf("Healthcheck: http://localhost:%s/health", port)
	log.Printf("================================================================")

	if err := app.Listen(":" + port); err != nil {
		log.Fatalf("Error al iniciar el servidor Fiber: %v", err)
	}
}
