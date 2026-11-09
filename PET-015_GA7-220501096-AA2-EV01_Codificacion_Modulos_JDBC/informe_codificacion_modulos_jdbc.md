# Informe Técnico: Codificación de Módulos del Software con Java JDBC y Arquitectura DAO
## Evidencia: GA7-220501096-AA2-EV01

---

### 🏛️ Identificación Institucional y Formativa
- **Institución:** Servicio Nacional de Aprendizaje (SENA)
- **Centro de Formación:** Centro de Teleinformática y Producción Industrial (CTPI) - Regional Cauca
- **Programa:** Análisis y Desarrollo de Software (ADSO) - Modalidad 100% Virtual
- **Ficha de Caracterización:** 228118
- **Aprendiz:** Karen Yuliana Campo
- **Ubicación:** Popayán, Cauca, Colombia
- **Actividad de Aprendizaje:** GA7-220501096-AA2: Aplicar estándares de codificación, de acuerdo con el diseño.
- **Instrumento de Evaluación:** IE-GA7-220501096-AA2-EV01
- **Fecha de Entrega:** Noviembre 2026

---

### 1. Introducción y Objetivos

En la fase de ejecución del ciclo de vida del software (AP7: Codificar los módulos del software), la persistencia de datos mediante **Java Database Connectivity (JDBC)** constituye el mecanismo estándar fundamental para conectar aplicaciones empresariales orientadas a objetos con sistemas de gestión de bases de datos relacionales (RDBMS).

El presente proyecto formativo da cumplimiento a la evidencia **GA7-220501096-AA2-EV01**, desarrollando el módulo backend de persistencia del sistema de información de la **Pizzería Bella Italia**, tomando como base el modelo relacional físico establecido previamente (`GA6-220501096-AA2-EV03.tsql`) e implementando la arquitectura de software **DAO (Data Access Object)** bajo estándares de codificación rigurosos y orquestación contenerizada con **Docker y Docker Compose**.

#### Objetivos Específicos:
1. Establecer la conexión con bases de datos relacionales (MariaDB / MySQL) mediante el API JDBC de Java 17.
2. Implementar una arquitectura en capas desacoplada: Entidades del Modelo de Dominio, Utilidades de Conexión, Objetos de Acceso a Datos (DAO) y Capa de Aplicación.
3. Desarrollar las cuatro operaciones elementales de persistencia (**CRUD: Create, Read, Update, Delete**) para las entidades centrales del negocio: `Clientes`, `Pizzas` y `Pedidos`.
4. Cumplir estrictamente con los estándares de nomenclatura y Clean Code para variables, métodos, clases y paquetes.
5. Garantizar la seguridad contra inyecciones SQL mediante el uso sistemático de `PreparedStatement` y el manejo transaccional ACID (`commit` y `rollback`).
6. Orquestar la infraestructura con Docker Compose para aislar el motor de base de datos y el runtime de compilación sin saturar el sistema host.

---

### 2. Estándares de Codificación Aplicados

De acuerdo con lo establecido en la Guía de Aprendizaje 7 y el componente formativo *Desarrollo de aplicaciones web con Java (CF20)*, el código fuente se rige bajo los siguientes convenios internacionales:

| Elemento | Convención de Nomenclatura | Ejemplo en el Código | Justificación Técnica |
|---|---|---|---|
| **Paquetes** | Notación inversa de dominio, todo minúsculas sin guiones | `com.sena.pizzeria.model`<br>`com.sena.pizzeria.dao`<br>`com.sena.pizzeria.util`<br>`com.sena.pizzeria.app` | Evita colisiones de nombres globales en el ecosistema Java y asegura modularidad. |
| **Clases** | `PascalCase`, sustantivos singulares | `Cliente`, `Pizza`, `Pedido`, `DetallePedido`, `ConexionBD`, `ClienteDAO` | Claridad semántica, fácil identificación de tipos y compatibilidad con Java Beans. |
| **Métodos** | `camelCase`, verbos en infinitivo que denotan acción | `insertar()`, `consultarPorId()`, `listarTodos()`, `actualizar()`, `eliminar()` | Expresa claramente la responsabilidad del método respetando el principio de responsabilidad única (SRP). |
| **Variables / Atributos** | `camelCase`, descriptivas, sin abreviaturas crípticas | `idCliente`, `nombrePizza`, `filasAfectadas`, `detalles` | Legibilidad inmediata y facilidad de mantenimiento. |
| **Constantes** | `UPPER_SNAKE_CASE` con modificadores `static final` | `SQL_INSERT`, `DEFAULT_HOST`, `MARIADB_DRIVER` | Inmutabilidad clara a nivel de compilador. |

---

### 3. Arquitectura del Módulo Backend (`PizzeriaBackend`)

El proyecto se diseñó bajo una arquitectura en capas orientada al dominio:

```
PizzeriaBackend/
├── pom.xml                                      (Configuración Maven, Java 17, drivers y JUnit 5)
└── src/
    ├── main/
    │   └── java/
    │       └── com/sena/pizzeria/
    │           ├── model/                       (Capa de Dominio / POO)
    │           │   ├── Cliente.java             (Entidad Cliente con serialización y encapsulamiento)
    │           │   ├── Pizza.java               (Entidad Pizza con catálogo y precios)
    │           │   ├── Pedido.java              (Entidad Pedido - Cabecera de orden)
    │           │   └── DetallePedido.java       (Línea de ítem de pedido)
    │           ├── util/                        (Capa de Infraestructura / Conexión)
    │           │   └── ConexionBD.java          (Factoría JDBC Singleton con soporte para variables de entorno)
    │           ├── dao/                         (Capa de Acceso a Datos / Patrón DAO)
    │           │   ├── ClienteDAO.java          (Operaciones CRUD para Clientes)
    │           │   ├── PizzaDAO.java            (Operaciones CRUD para Catálogo de Pizzas)
    │           │   └── PedidoDAO.java           (Operaciones CRUD y Transacciones ACID para Pedidos)
    │           └── app/                         (Capa de Presentación / Aplicación)
    │               └── Main.java                (Demostración en vivo de todas las operaciones)
    └── test/
        └── java/
            └── com/sena/pizzeria/
                └── PizzeriaCRUDTest.java        (Pruebas unitarias automatizadas con JUnit 5)
```

---

### 4. Implementación de Operaciones CRUD y Conectividad JDBC

#### 4.1. Conexión JDBC Resiliente (`ConexionBD.java`)
La clase `ConexionBD` implementa un conector parametrizado que detecta automáticamente si el entorno se ejecuta dentro de la red Docker (`DB_HOST=sena-pizzeria-db`) o en un entorno local, soportando tanto controladores MariaDB como MySQL nativo:

```java
public static Connection getConexion() throws SQLException {
    String host = System.getenv("DB_HOST") != null ? System.getenv("DB_HOST") : "localhost";
    String port = System.getenv("DB_PORT") != null ? System.getenv("DB_PORT") : "3306";
    String database = System.getenv("DB_NAME") != null ? System.getenv("DB_NAME") : "pizzeria";
    String user = System.getenv("DB_USER") != null ? System.getenv("DB_USER") : "karen";
    String password = System.getenv("DB_PASS") != null ? System.getenv("DB_PASS") : "choco";

    String url = String.format("jdbc:mariadb://%s:%s/%s?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=America/Bogota",
            host, port, database);
    return DriverManager.getConnection(url, user, password);
}
```

#### 4.2. Operaciones CRUD en DAO (Ejemplo: `ClienteDAO.java`)
Todas las consultas utilizan `PreparedStatement` para garantizar que los parámetros enviados por el usuario sean tratados estrictamente como datos literales, imposibilitando ataques de inyección SQL:

- **Inserción (Create):**
  ```java
  public boolean insertar(Cliente cliente) {
      String sql = "INSERT INTO CLIENTES (Nombre, Telefono, Direccion) VALUES (?, ?, ?)";
      try (Connection conn = ConexionBD.getConexion();
           PreparedStatement stmt = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS)) {
          stmt.setString(1, cliente.getNombre());
          stmt.setString(2, cliente.getTelefono());
          stmt.setString(3, cliente.getDireccion());
          if (stmt.executeUpdate() > 0) {
              try (ResultSet rs = stmt.getGeneratedKeys()) {
                  if (rs.next()) cliente.setIdCliente(rs.getInt(1));
              }
              return true;
          }
      } catch (SQLException e) { ... }
      return false;
  }
  ```

- **Consulta (Read):** Métodos `consultarPorId(int id)` y `listarTodos()` con mapeo tipado hacia objetos `Cliente`.
- **Actualización (Update):** `UPDATE CLIENTES SET Nombre = ?, Telefono = ?, Direccion = ? WHERE ID_Cliente = ?`.
- **Eliminación (Delete):** `DELETE FROM CLIENTES WHERE ID_Cliente = ?`.

#### 4.3. Transaccionalidad ACID en `PedidoDAO.java`
Para garantizar que una orden de pedido no quede inconsistente si ocurre una falla al insertar sus detalles, se implementó control explícito de transacciones:

```java
conn.setAutoCommit(false); // Inicio de transacción atómica
// 1. Insertar en tabla PEDIDOS y obtener ID_Pedido generado
// 2. Insertar batch en tabla DETALLE_PEDIDO
conn.commit(); // Confirmación atómica si todo fue exitoso
// En caso de excepción: conn.rollback();
```

---

### 5. Orquestación Contenerizada con Docker Compose

Para evitar instalar entornos JDK pesados o servicios de base de datos directos en la máquina host del usuario, se implementó un archivo orquestador general `docker-compose.yml`:

```yaml
services:
  db:
    image: mariadb:10.5
    container_name: sena-pizzeria-db
    environment:
      MYSQL_ROOT_PASSWORD: choco
      MYSQL_DATABASE: pizzeria
      MYSQL_USER: karen
      MYSQL_PASSWORD: choco
    volumes:
      - ./docker/mariadb/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
      - pizzeria_db_data:/var/lib/mysql

  backend-java:
    image: maven:3.9.6-eclipse-temurin-17-alpine
    container_name: sena-backend-java
    working_dir: /app/PizzeriaBackend
    environment:
      DB_HOST: db
      DB_USER: karen
      DB_PASS: choco
    volumes:
      - .:/app
      - maven_m2_cache:/root/.m2
```

---

### 6. Resultados de Ejecución y Pruebas Unitarias

#### 6.1. Pruebas Automatizadas con JUnit 5 (`PizzeriaCRUDTest.java`)
Se ejecutaron las pruebas dentro del contenedor Maven arrojando un resultado de **100% aprobadas (0 fallos, 0 errores)**:

```
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.sena.pizzeria.PizzeriaCRUDTest
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.511 s
[INFO] Results:
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0
[INFO] BUILD SUCCESS
```

#### 6.2. Demostración en Vivo en Consola (`Main.java`)
La ejecución de la clase principal confirmó la realización exitosa de cada operación en tiempo real:
- **[1/4] JDBC:** Conexión exitosa a MariaDB 10.5.
- **[2/4] CLIENTES:** Creación de cliente de prueba (ID 5), consulta, actualización de dirección y eliminación limpia.
- **[3/4] PIZZAS:** Creación de pizza en catálogo, actualización de precio ($58,000) y eliminación.
- **[4/4] PEDIDOS:** Creación transaccional de orden con 2 detalles, actualización de estado a 'Entregado' y purga de prueba.

---

### 7. Matriz de Cumplimiento de la Rúbrica SENA (IE-GA7-220501096-AA2-EV01)

| Criterio Evaluado | Estado | Evidencia Aportada |
|---|:---:|---|
| 1. Codifica los módulos del software teniendo en cuenta los artefactos del ciclo de software previos. | **CUMPLE** | Implementación alineada con el modelo relacional físico `pizzeria` (`GA6-220501096-AA2-EV03.tsql`). |
| 2. Realiza conexiones con bases de datos por medio de JDBC. | **CUMPLE** | Clase `ConexionBD` con driver MariaDB/MySQL y manejo robusto de excepciones. |
| 3. Aplica estándares de codificación (variables, métodos, clases, paquetes). | **CUMPLE** | Arquitectura en paquetes `com.sena.pizzeria.*`, clases en PascalCase y métodos en camelCase. |
| 4. Desarrolla funcionalidades de inserción, consulta, actualización y eliminación (CRUD). | **CUMPLE** | Operaciones CRUD completas en `ClienteDAO`, `PizzaDAO` y `PedidoDAO`. |
| 5. Se crea el proyecto utilizando herramientas de versionamiento. | **CUMPLE** | Proyecto versionado en Git y vinculado al repositorio oficial de GitHub. |
| 6. Entrega en carpeta comprimida con nombre reglamentario (ZIP). | **CUMPLE** | Archivo `KARENCAMPO_AA2_EV01.zip` con código, enlace de repo y documentación. |

---

### 8. Conclusiones
1. Se implementó una solución de backend en Java moderna, modular y segura, aplicando patrones de diseño consolidados (DAO y Factory) y buenas prácticas de persistencia con JDBC.
2. La utilización de Docker Compose permitió aislar completamente el entorno de desarrollo y la base de datos MariaDB, garantizando reproducibilidad sin intervenir la configuración del sistema operativo host.
3. El proyecto se entrega con suite de pruebas unitarias al 100% en verde, archivo ejecutable de consola, paquete comprimido normativo y documentación formal para Zajuna.
