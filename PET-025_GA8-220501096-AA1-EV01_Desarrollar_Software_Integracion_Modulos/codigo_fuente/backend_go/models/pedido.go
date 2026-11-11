package models

import "time"

// ItemPedido representa una pizza o producto dentro del carrito y la orden
type ItemPedido struct {
	Codigo         string   `json:"codigo" bson:"codigo"`
	PizzaCodigo    string   `json:"pizzaCodigo" bson:"-"`
	Nombre         string   `json:"nombre" bson:"nombre"`
	Tamano         string   `json:"tamano" bson:"tamano"` // personal, mediana, familiar
	PrecioUnitario float64  `json:"precioUnitario" bson:"precioUnitario"`
	Cantidad       int      `json:"cantidad" bson:"cantidad"`
	Adiciones      []string `json:"adiciones" bson:"adiciones"`
	TotalItem      float64  `json:"totalItem" bson:"totalItem"`
}

// HistorialEstado documenta la trazabilidad del pedido a lo largo del tiempo
type HistorialEstado struct {
	Estado string    `json:"estado" bson:"estado"`
	Fecha  time.Time `json:"fecha" bson:"fecha"`
	Nota   string    `json:"nota" bson:"nota"`
}

// DescuentoCupon almacena el descuento aplicado por cupón promocional
type DescuentoCupon struct {
	Codigo string `json:"codigo" bson:"codigo"`
	Valor  int    `json:"valor" bson:"valor"`
}

// Pedido representa la orden completa con items, pagos y ciclo de vida de estados
type Pedido struct {
	NumeroPedido          string            `json:"numeroPedido" bson:"numeroPedido"`
	ClienteUsuario        string            `json:"clienteUsuario" bson:"clienteUsuario"`
	ClienteNombre         string            `json:"clienteNombre" bson:"clienteNombre"`
	ClienteTelefono       string            `json:"clienteTelefono" bson:"clienteTelefono"`
	DireccionEntrega      string            `json:"direccionEntrega" bson:"direccionEntrega"`
	Items                 []ItemPedido      `json:"items" bson:"items"`
	Subtotal              int               `json:"subtotal" bson:"subtotal"`
	DescuentoCupon        *DescuentoCupon   `json:"descuentoCupon,omitempty" bson:"descuentoCupon,omitempty"`
	CostoEnvio            int               `json:"costoEnvio" bson:"costoEnvio"`
	Total                 int               `json:"total" bson:"total"`
	MedioPago             string            `json:"medioPago" bson:"medioPago"` // EFECTIVO, TARJETA_CREDITO, PSE_NEQUI, DAVIPLATA
	EstadoPago            string            `json:"estadoPago" bson:"estadoPago"` // PENDIENTE, APROBADO, RECHAZADO
	ReferenciaPago        string            `json:"referenciaPago" bson:"referenciaPago"`
	Estado                string            `json:"estado" bson:"estado"` // RECIBIDO, EN_PREPARACION, EN_HORNO, EN_CAMINO, ENTREGADO, CANCELADO
	HistorialEstados      []HistorialEstado `json:"historialEstados" bson:"historialEstados"`
	FechaCreacion         time.Time         `json:"fechaCreacion" bson:"fechaCreacion"`
	TiempoEstimadoMinutos int               `json:"tiempoEstimadoMinutos" bson:"tiempoEstimadoMinutos"`
}

// CrearPedidoRequest define el payload recibido al realizar un checkout
type CrearPedidoRequest struct {
	DireccionEntrega string       `json:"direccionEntrega"`
	DireccionEnvio   string       `json:"direccionEnvio"`
	Items            []ItemPedido `json:"items"`
	CodigoCupon      string       `json:"codigoCupon"`
	CuponCodigo      string       `json:"cuponCodigo"`
	MedioPago        string       `json:"medioPago"`
	MetodoPago       string       `json:"metodoPago"`
}

// ActualizarEstadoRequest define la actualización realizada por el administrador
type ActualizarEstadoRequest struct {
	Estado string `json:"estado"` // RECIBIDO, EN_PREPARACION, EN_HORNO, EN_CAMINO, ENTREGADO, CANCELADO
	Nota   string `json:"nota"`
}
