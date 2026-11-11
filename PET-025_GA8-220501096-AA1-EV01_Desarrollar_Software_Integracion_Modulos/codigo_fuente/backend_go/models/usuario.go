package models

import "time"

// DireccionUsuario representa una dirección de entrega guardada por el cliente
type DireccionUsuario struct {
	Alias     string `json:"alias" bson:"alias"`
	Direccion string `json:"direccion" bson:"direccion"`
	Ciudad    string `json:"ciudad" bson:"ciudad"`
	Principal bool   `json:"principal" bson:"principal"`
}

// Usuario modela los administradores y clientes del sistema
type Usuario struct {
	Usuario       string             `json:"usuario" bson:"usuario"`
	Email         string             `json:"email" bson:"email"`
	Nombre        string             `json:"nombre" bson:"nombre"`
	Telefono      string             `json:"telefono" bson:"telefono"`
	Rol           string             `json:"rol" bson:"rol"` // "ADMIN" o "CLIENTE"
	PasswordHash  string             `json:"-" bson:"passwordHash"`
	Activo        bool               `json:"activo" bson:"activo"`
	Direcciones   []DireccionUsuario `json:"direcciones" bson:"direcciones"`
	FechaCreacion time.Time          `json:"fechaCreacion" bson:"fechaCreacion"`
}

// LoginRequest estructura las credenciales enviadas para iniciar sesión
type LoginRequest struct {
	Usuario  string `json:"usuario"`
	Password string `json:"password"`
}

// RegisterRequest estructura los datos para crear una nueva cuenta
type RegisterRequest struct {
	Usuario   string `json:"usuario"`
	Email     string `json:"email"`
	Nombre    string `json:"nombre"`
	Telefono  string `json:"telefono"`
	Password  string `json:"password"`
	Rol       string `json:"rol"`
	Direccion string `json:"direccion"`
}

// AuthResponse contiene la confirmación y el token JWT
type AuthResponse struct {
	Success   bool     `json:"success"`
	Mensaje   string   `json:"mensaje"`
	Token     string   `json:"token,omitempty"`
	TokenType string   `json:"tokenType,omitempty"`
	ExpiresIn string   `json:"expiresIn,omitempty"`
	Usuario   *Usuario `json:"usuario,omitempty"`
}
