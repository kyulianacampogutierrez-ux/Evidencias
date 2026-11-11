package models

// Categoria representa las secciones de la carta de la pizzería
type Categoria struct {
	Codigo      string `json:"codigo" bson:"codigo"`
	Nombre      string `json:"nombre" bson:"nombre"`
	Descripcion string `json:"descripcion" bson:"descripcion"`
	Activa      bool   `json:"activa" bson:"activa"`
}
