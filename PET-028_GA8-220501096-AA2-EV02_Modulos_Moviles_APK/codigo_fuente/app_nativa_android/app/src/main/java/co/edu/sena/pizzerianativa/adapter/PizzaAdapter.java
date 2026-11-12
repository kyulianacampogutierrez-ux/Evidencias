package co.edu.sena.pizzerianativa.adapter;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import co.edu.sena.pizzerianativa.R;
import co.edu.sena.pizzerianativa.model.Pizza;
import java.util.List;

/**
 * Adaptador RecyclerView para el catálogo de pizzas artesanales.
 * Guía 8 - GA8-220501096-AA2-EV01
 */
public class PizzaAdapter extends RecyclerView.Adapter<PizzaAdapter.PizzaViewHolder> {

    private final List<Pizza> listaPizzas;
    private final OnPizzaClickListener listener;

    public interface OnPizzaClickListener {
        void onPizzaClick(Pizza pizza);
    }

    public PizzaAdapter(List<Pizza> listaPizzas, OnPizzaClickListener listener) {
        this.listaPizzas = listaPizzas;
        this.listener = listener;
    }

    @NonNull
    @Override
    public PizzaViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_pizza, parent, false);
        return new PizzaViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull PizzaViewHolder holder, int position) {
        Pizza pizza = listaPizzas.get(position);
        holder.tvNombre.setText(pizza.getNombre());
        holder.tvDescripcion.setText(pizza.getDescripcion());
        holder.tvPrecio.setText(pizza.getPrecioFormateado());
        holder.tvCategoria.setText(pizza.getCategoria());

        holder.itemView.setOnClickListener(v -> {
            if (listener != null) {
                listener.onPizzaClick(pizza);
            }
        });
    }

    @Override
    public int getItemCount() {
        return listaPizzas.size();
    }

    static class PizzaViewHolder extends RecyclerView.ViewHolder {
        TextView tvNombre;
        TextView tvDescripcion;
        TextView tvPrecio;
        TextView tvCategoria;

        public PizzaViewHolder(@NonNull View itemView) {
            super(itemView);
            tvNombre = itemView.findViewById(R.id.tvPizzaName);
            tvDescripcion = itemView.findViewById(R.id.tvPizzaDesc);
            tvPrecio = itemView.findViewById(R.id.tvPizzaPrice);
            tvCategoria = itemView.findViewById(R.id.tvPizzaCategory);
        }
    }
}
