package models

import "time"

// Cupon modela un código de descuento con porcentaje y fecha límite
type Cupon struct {
	Codigo       string    `json:"codigo" bson:"codigo"`
	Descripcion  string    `json:"descripcion" bson:"descripcion"`
	Porcentaje   int       `json:"porcentaje" bson:"porcentaje"`
	MaxDescuento int       `json:"maxDescuento" bson:"maxDescuento"`
	Activo       bool      `json:"activo" bson:"activo"`
	Expiracion   time.Time `json:"expiracion" bson:"expiracion"`
}

// ValidarCuponRequest estructura la petición para consultar validez de un cupón
type ValidarCuponRequest struct {
	Codigo   string  `json:"codigo"`
	Subtotal float64 `json:"subtotal"`
}

// ValidarCuponResponse estructura el resultado del cálculo del cupón
type ValidarCuponResponse struct {
	Valido             bool    `json:"valido"`
	Codigo             string  `json:"codigo"`
	Porcentaje         float64 `json:"porcentaje"`
	Descuento          float64 `json:"descuento"`
	DescuentoCalculado float64 `json:"descuentoCalculado"`
	Mensaje            string  `json:"mensaje"`
}
