package com.sena.pizzeria.model;

import java.io.Serializable;
import java.util.Objects;

/**
 * Entidad de dominio que representa una Pizza en el catálogo de productos.
 * Cumple con estándares de nomenclatura JavaBeans y POO.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class Pizza implements Serializable {
    private static final long serialVersionUID = 1L;

    private int idPizza;
    private String nombrePizza;
    private String tamaño;
    private double precio;

    public Pizza() {
    }

    public Pizza(String nombrePizza, String tamaño, double precio) {
        this.nombrePizza = nombrePizza;
        this.tamaño = tamaño;
        this.precio = precio;
    }

    public Pizza(int idPizza, String nombrePizza, String tamaño, double precio) {
        this.idPizza = idPizza;
        this.nombrePizza = nombrePizza;
        this.tamaño = tamaño;
        this.precio = precio;
    }

    public int getIdPizza() {
        return idPizza;
    }

    public void setIdPizza(int idPizza) {
        this.idPizza = idPizza;
    }

    public String getNombrePizza() {
        return nombrePizza;
    }

    public void setNombrePizza(String nombrePizza) {
        this.nombrePizza = nombrePizza;
    }

    public String getTamaño() {
        return tamaño;
    }

    public void setTamaño(String tamaño) {
        this.tamaño = tamaño;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pizza pizza = (Pizza) o;
        return idPizza == pizza.idPizza &&
               Double.compare(pizza.precio, precio) == 0 &&
               Objects.equals(nombrePizza, pizza.nombrePizza);
    }

    @Override
    public int hashCode() {
        return Objects.hash(idPizza, nombrePizza, precio);
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "idPizza=" + idPizza +
                ", nombrePizza='" + nombrePizza + '\'' +
                ", tamaño='" + tamaño + '\'' +
                ", precio=" + precio +
                '}';
    }
}
