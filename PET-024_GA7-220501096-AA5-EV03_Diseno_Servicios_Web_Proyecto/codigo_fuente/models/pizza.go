package models

// PreciosPizza define la estructura de precios por tamaño
type PreciosPizza struct {
	Personal int `json:"personal" bson:"personal"`
	Mediana  int `json:"mediana" bson:"mediana"`
	Familiar int `json:"familiar" bson:"familiar"`
}

// AdicionPizza define una adición o personalización disponible
type AdicionPizza struct {
	Nombre string `json:"nombre" bson:"nombre"`
	Precio int    `json:"precio" bson:"precio"`
}

// Pizza representa un producto del catálogo (carta) de la pizzería
type Pizza struct {
	Codigo               string         `json:"codigo" bson:"codigo"`
	Nombre               string         `json:"nombre" bson:"nombre"`
	Categoria            string         `json:"categoria" bson:"categoria"`
	Descripcion          string         `json:"descripcion" bson:"descripcion"`
	ImagenURL            string         `json:"imagenUrl" bson:"imagenUrl"`
	Precios              PreciosPizza   `json:"precios" bson:"precios"`
	Ingredientes         []string       `json:"ingredientes" bson:"ingredientes"`
	AdicionesDisponibles []AdicionPizza `json:"adicionesDisponibles" bson:"adicionesDisponibles"`
	Destacada            bool           `json:"destacada" bson:"destacada"`
	Disponible           bool           `json:"disponible" bson:"disponible"`
	CalificacionPromedio float64        `json:"calificacionPromedio" bson:"calificacionPromedio"`
	NumCalificaciones    int            `json:"numCalificaciones" bson:"numCalificaciones"`
}
