package co.edu.sena.pizzerianativa.model;

/**
 * Modelo de datos Pizza para la aplicación móvil nativa Android 14.
 * Proyecto formativo: Pizzería Gourmet Bella Italia Popayán.
 * Aprendiz: Karen Yuliana Campo - Ficha 3186681 - CTPI Popayán
 */
public class Pizza {
    private String id;
    private String nombre;
    private String descripcion;
    private String categoria;
    private double precio;

    public Pizza(String id, String nombre, String descripcion, String categoria, double precio) {
        this.id = id;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.categoria = categoria;
        this.precio = precio;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public String getCategoria() {
        return categoria;
    }

    public double getPrecio() {
        return precio;
    }

    public String getPrecioFormateado() {
        return String.format("$%,.0f COP", precio);
    }
}
