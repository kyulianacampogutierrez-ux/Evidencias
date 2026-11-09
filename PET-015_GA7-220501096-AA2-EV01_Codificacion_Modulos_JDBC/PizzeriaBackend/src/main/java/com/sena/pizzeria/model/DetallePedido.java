package com.sena.pizzeria.model;

import java.io.Serializable;
import java.util.Objects;

/**
 * Entidad de dominio que representa un Detalle de Pedido (línea de factura/orden).
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class DetallePedido implements Serializable {
    private static final long serialVersionUID = 1L;

    private int idDetalle;
    private int cantidad;
    private double subtotal;
    private int idPedido;
    private int idPizza;

    public DetallePedido() {
    }

    public DetallePedido(int cantidad, double subtotal, int idPedido, int idPizza) {
        this.cantidad = cantidad;
        this.subtotal = subtotal;
        this.idPedido = idPedido;
        this.idPizza = idPizza;
    }

    public DetallePedido(int idDetalle, int cantidad, double subtotal, int idPedido, int idPizza) {
        this.idDetalle = idDetalle;
        this.cantidad = cantidad;
        this.subtotal = subtotal;
        this.idPedido = idPedido;
        this.idPizza = idPizza;
    }

    public int getIdDetalle() {
        return idDetalle;
    }

    public void setIdDetalle(int idDetalle) {
        this.idDetalle = idDetalle;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public double getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(double subtotal) {
        this.subtotal = subtotal;
    }

    public int getIdPedido() {
        return idPedido;
    }

    public void setIdPedido(int idPedido) {
        this.idPedido = idPedido;
    }

    public int getIdPizza() {
        return idPizza;
    }

    public void setIdPizza(int idPizza) {
        this.idPizza = idPizza;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        DetallePedido that = (DetallePedido) o;
        return idDetalle == that.idDetalle &&
               idPedido == that.idPedido &&
               idPizza == that.idPizza;
    }

    @Override
    public int hashCode() {
        return Objects.hash(idDetalle, idPedido, idPizza);
    }

    @Override
    public String toString() {
        return "DetallePedido{" +
                "idDetalle=" + idDetalle +
                ", cantidad=" + cantidad +
                ", subtotal=" + subtotal +
                ", idPedido=" + idPedido +
                ", idPizza=" + idPizza +
                '}';
    }
}
