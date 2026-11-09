package com.sena.pizzeria.model;

import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * Entidad de dominio que representa un Pedido en la Pizzería Bella Italia.
 * Representa el encabezado de la orden de venta.
 * 
 * @author Karen Yuliana Campo
 * @version 1.0.0
 */
public class Pedido implements Serializable {
    private static final long serialVersionUID = 1L;

    private int idPedido;
    private LocalDateTime fecha;
    private double total;
    private int idCliente;
    private String estado;
    private List<DetallePedido> detalles = new ArrayList<>();

    public Pedido() {
        this.fecha = LocalDateTime.now();
        this.estado = "En Preparación";
    }

    public Pedido(int idCliente, double total, String estado) {
        this.fecha = LocalDateTime.now();
        this.idCliente = idCliente;
        this.total = total;
        this.estado = estado;
    }

    public Pedido(int idPedido, LocalDateTime fecha, double total, int idCliente, String estado) {
        this.idPedido = idPedido;
        this.fecha = fecha;
        this.total = total;
        this.idCliente = idCliente;
        this.estado = estado;
    }

    public int getIdPedido() {
        return idPedido;
    }

    public void setIdPedido(int idPedido) {
        this.idPedido = idPedido;
    }

    public LocalDateTime getFecha() {
        return fecha;
    }

    public void setFecha(LocalDateTime fecha) {
        this.fecha = fecha;
    }

    public double getTotal() {
        return total;
    }

    public void setTotal(double total) {
        this.total = total;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getEstado() {
        return estado;
    }

    public void setEstado(String estado) {
        this.estado = estado;
    }

    public List<DetallePedido> getDetalles() {
        return detalles;
    }

    public void setDetalles(List<DetallePedido> detalles) {
        this.detalles = detalles;
    }

    public void agregarDetalle(DetallePedido detalle) {
        this.detalles.add(detalle);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pedido pedido = (Pedido) o;
        return idPedido == pedido.idPedido && idCliente == pedido.idCliente;
    }

    @Override
    public int hashCode() {
        return Objects.hash(idPedido, idCliente);
    }

    @Override
    public String toString() {
        return "Pedido{" +
                "idPedido=" + idPedido +
                ", fecha=" + fecha +
                ", total=" + total +
                ", idCliente=" + idCliente +
                ", estado='" + estado + '\'' +
                '}';
    }
}
