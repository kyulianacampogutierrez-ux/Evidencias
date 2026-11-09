package com.sena.pizzeria.model;

import java.io.Serializable;
import java.util.Objects;

/**
 * Entidad de dominio que representa a un Cliente en el sistema de la Pizzería.
 * Cumple con estándares de nomenclatura JavaBeans y POO.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class Cliente implements Serializable {
    private static final long serialVersionUID = 1L;

    private int idCliente;
    private String nombre;
    private String telefono;
    private String direccion;

    public Cliente() {
    }

    public Cliente(String nombre, String telefono, String direccion) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.direccion = direccion;
    }

    public Cliente(int idCliente, String nombre, String telefono, String direccion) {
        this.idCliente = idCliente;
        this.nombre = nombre;
        this.telefono = telefono;
        this.direccion = direccion;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Cliente cliente = (Cliente) o;
        return idCliente == cliente.idCliente &&
               Objects.equals(nombre, cliente.nombre) &&
               Objects.equals(telefono, cliente.telefono);
    }

    @Override
    public int hashCode() {
        return Objects.hash(idCliente, nombre, telefono);
    }

    @Override
    public String toString() {
        return "Cliente{" +
                "idCliente=" + idCliente +
                ", nombre='" + nombre + '\'' +
                ", telefono='" + telefono + '\'' +
                ", direccion='" + direccion + '\'' +
                '}';
    }
}
