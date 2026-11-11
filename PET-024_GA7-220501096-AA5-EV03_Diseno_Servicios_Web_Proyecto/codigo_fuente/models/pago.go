package models

// ProcesarPagoRequest modela la pasarela de pagos simulada
type ProcesarPagoRequest struct {
	NumeroPedido string  `json:"numeroPedido"`
	MedioPago    string  `json:"medioPago"` // EFECTIVO, TARJETA_CREDITO, PSE_NEQUI, DAVIPLATA
	Metodo       string  `json:"metodo"`
	Titular      string  `json:"titular"`
	NumeroDoc    string  `json:"numeroDoc"`
	Telefono     string  `json:"telefono"`
	Monto        float64 `json:"monto"`
}

// ComprobantePago representa el recibo digital emitido al confirmar la transacción
type ComprobantePago struct {
	Referencia     string  `json:"referencia"`
	NumeroPedido   string  `json:"numeroPedido"`
	MedioPago      string  `json:"medioPago"`
	Monto          float64 `json:"monto"`
	EstadoPago     string  `json:"estadoPago"` // APROBADO, PENDIENTE
	Mensaje        string  `json:"mensaje"`
	FechaOperacion string  `json:"fechaOperacion"`
}
