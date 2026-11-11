package config

import (
	"context"
	"log"
	"os"
	"time"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var (
	DB     *mongo.Database
	Client *mongo.Client
)

// ConnectDB inicializa el pool de conexiones con MongoDB
func ConnectDB() *mongo.Database {
	mongoURI := os.Getenv("MONGO_URI")
	if mongoURI == "" {
		mongoURI = "mongodb://localhost:27017"
	}

	dbName := os.Getenv("MONGO_DB")
	if dbName == "" {
		dbName = "pizzeria_db"
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	clientOpts := options.Client().ApplyURI(mongoURI)
	client, err := mongo.Connect(ctx, clientOpts)
	if err != nil {
		log.Fatalf("Error al conectar con MongoDB (%s): %v", mongoURI, err)
	}

	// Ping al servidor MongoDB
	if err := client.Ping(ctx, nil); err != nil {
		log.Printf("Advertencia: No se pudo verificar ping inicial con MongoDB (%s): %v", mongoURI, err)
	} else {
		log.Printf("Conexión exitosa con MongoDB en base de datos: %s", dbName)
	}

	Client = client
	DB = client.Database(dbName)
	return DB
}

func GetCollection(name string) *mongo.Collection {
	if DB == nil {
		ConnectDB()
	}
	return DB.Collection(name)
}
