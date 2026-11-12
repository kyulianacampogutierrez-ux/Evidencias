package co.edu.sena.pizzerianativa;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import co.edu.sena.pizzerianativa.adapter.PizzaAdapter;
import co.edu.sena.pizzerianativa.model.Pizza;
import java.util.ArrayList;
import java.util.List;

/**
 * Actividad Principal Nativa Android 14 (API 34).
 * Evidencia: GA8-220501096-AA2-EV01 - Taller Tecnologías Emergentes y Disruptivas Móviles.
 * Aprendiz: Karen Yuliana Campo | Ficha: 3186681 | Centro: CTPI Popayán - Regional Cauca.
 */
public class MainActivity extends AppCompatActivity {

    private TextView tvStatus;
    private TextView tvWelcomeMessage;
    private RecyclerView rvPizzas;
    private Button btnVerCatalogo;
    private Button btnValidarCupon;
    private Button btnSimularPedido;

    private List<Pizza> pizzas;
    private PizzaAdapter pizzaAdapter;
    private boolean cuponAplicado = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar componentes UI
        tvStatus = findViewById(R.id.tvStatus);
        tvWelcomeMessage = findViewById(R.id.tvWelcomeMessage);
        rvPizzas = findViewById(R.id.rvPizzas);
        btnVerCatalogo = findViewById(R.id.btnVerCatalogo);
        btnValidarCupon = findViewById(R.id.btnValidarCupon);
        btnSimularPedido = findViewById(R.id.btnSimularPedido);

        // Configurar RecyclerView
        rvPizzas.setLayoutManager(new LinearLayoutManager(this));
        inicializarCatalogo();

        pizzaAdapter = new PizzaAdapter(pizzas, pizza -> {
            String mensaje = "Seleccionaste: " + pizza.getNombre() + " (" + pizza.getPrecioFormateado() + ")";
            Toast.makeText(MainActivity.this, mensaje, Toast.LENGTH_SHORT).show();
            tvStatus.setText("🍕 Pizza seleccionada: " + pizza.getNombre());
        });
        rvPizzas.setAdapter(pizzaAdapter);

        // Eventos interactivos requeridos por Guía 8
        btnVerCatalogo.setOnClickListener(v -> {
            String msg = "Mostrando 4 especialidades gourmet artesanales Bella Italia Popayán.";
            Toast.makeText(MainActivity.this, msg, Toast.LENGTH_SHORT).show();
            tvStatus.setText("📋 Catálogo cargado con 4 pizzas artesanales");
        });

        btnValidarCupon.setOnClickListener(v -> {
            if (!cuponAplicado) {
                cuponAplicado = true;
                btnValidarCupon.setText("Cupón SENA2026 Aplicado (-15%)");
                tvStatus.setText("🎉 Descuento SENA2026 del 15% aplicado a todos los pedidos");
                Toast.makeText(MainActivity.this, "¡Cupón SENA2026 validado exitosamente (-15%)!", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(MainActivity.this, "El cupón SENA2026 ya se encuentra activo.", Toast.LENGTH_SHORT).show();
            }
        });

        btnSimularPedido.setOnClickListener(v -> {
            String orderId = "ORD-" + System.currentTimeMillis();
            String msg = "Pedido #" + orderId + " enviado a cocina en Popayán. Tiempo estimado: 25 min.";
            tvStatus.setText("🛵 Pedido en camino: " + orderId);
            Toast.makeText(MainActivity.this, msg, Toast.LENGTH_LONG).show();
        });
    }

    private void inicializarCatalogo() {
        pizzas = new ArrayList<>();
        pizzas.add(new Pizza("PZ01", "Margherita D.O.P.", "Pomodoro San Marzano, mozzarella fior di latte, albahaca fresca y AOVE.", "Gourmet Tradicional", 32000));
        pizzas.add(new Pizza("PZ02", "Quattro Formaggi", "Mozzarella, gorgonzola D.O.P., parmigiano reggiano y fontina fundido.", "Especialidad Quesos", 38000));
        pizzas.add(new Pizza("PZ03", "Diavola Artesanal", "Pomodoro, mozzarella fior di latte, salame piccante y orégano silvestre.", "Picante Gourmet", 35000));
        pizzas.add(new Pizza("PZ04", "Prosciutto e Funghi", "Mozzarella, jamón serrano curado, hongos frescos de temporada y trufa negra.", "Premium Reserva", 42000));
    }
}
