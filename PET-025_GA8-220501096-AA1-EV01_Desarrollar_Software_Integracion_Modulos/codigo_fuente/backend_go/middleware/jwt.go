package middleware

import (
	"errors"
	"os"
	"strings"
	"time"

	"github.com/gofiber/fiber/v2"
	"github.com/golang-jwt/jwt/v5"
	"pizzeria-backend-go/models"
)

var jwtSecretKey = []byte(getJWTSecret())

func getJWTSecret() string {
	secret := os.Getenv("JWT_SECRET")
	if secret == "" {
		return "SENA_ADSO_228118_BELLA_ITALIA_GO_FIBER_2026"
	}
	return secret
}

// CustomClaims extiende los claims estándar con los metadatos del usuario
type CustomClaims struct {
	Usuario string `json:"usuario"`
	Email   string `json:"email"`
	Nombre  string `json:"nombre"`
	Rol     string `json:"rol"`
	jwt.RegisteredClaims
}

// GenerateJWT genera un nuevo token firmado con expiración de 24 horas
func GenerateJWT(u *models.Usuario) (string, error) {
	claims := CustomClaims{
		Usuario: u.Usuario,
		Email:   u.Email,
		Nombre:  u.Nombre,
		Rol:     u.Rol,
		RegisteredClaims: jwt.RegisteredClaims{
			ExpiresAt: jwt.NewNumericDate(time.Now().Add(24 * time.Hour)),
			IssuedAt:  jwt.NewNumericDate(time.Now()),
			NotBefore: jwt.NewNumericDate(time.Now()),
			Issuer:    "sena-adso-pizzeria-go-fiber",
			Subject:   u.Usuario,
		},
	}

	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	return token.SignedString(jwtSecretKey)
}

// JWTMiddleware valida la cabecera Authorization Bearer en peticiones protegidas
func JWTMiddleware() fiber.Handler {
	return func(c *fiber.Ctx) error {
		authHeader := c.Get("Authorization")
		if authHeader == "" {
			return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
				"success": false,
				"error":   "UNAUTHORIZED",
				"mensaje": "Cabecera Authorization no suministrada. Se requiere token Bearer.",
			})
		}

		parts := strings.Split(authHeader, " ")
		if len(parts) != 2 || strings.ToLower(parts[0]) != "bearer" {
			return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
				"success": false,
				"error":   "UNAUTHORIZED",
				"mensaje": "Formato de autorización inválido. Debe ser: Bearer <TOKEN>",
			})
		}

		tokenString := parts[1]
		claims := &CustomClaims{}

		token, err := jwt.ParseWithClaims(tokenString, claims, func(token *jwt.Token) (interface{}, error) {
			if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
				return nil, errors.New("método de firma inesperado")
			}
			return jwtSecretKey, nil
		})

		if err != nil || !token.Valid {
			return c.Status(fiber.StatusUnauthorized).JSON(fiber.Map{
				"success": false,
				"error":   "UNAUTHORIZED",
				"mensaje": "Token de autenticación inválido o expirado.",
			})
		}

		// Almacenar datos en el contexto de Fiber
		c.Locals("usuario", claims.Usuario)
		c.Locals("rol", claims.Rol)
		c.Locals("nombre", claims.Nombre)
		c.Locals("email", claims.Email)

		return c.Next()
	}
}

// AdminOnlyMiddleware restringe el acceso exclusivamente a usuarios con rol ADMIN
func AdminOnlyMiddleware() fiber.Handler {
	return func(c *fiber.Ctx) error {
		rol, ok := c.Locals("rol").(string)
		if !ok || rol != "ADMIN" {
			return c.Status(fiber.StatusForbidden).JSON(fiber.Map{
				"success": false,
				"error":   "FORBIDDEN",
				"mensaje": "Acceso restringido: Se requieren privilegios de Administrador.",
			})
		}
		return c.Next()
	}
}
