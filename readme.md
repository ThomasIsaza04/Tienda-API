#  API E-Commerce Segura (FastAPI + JWT + RBAC)

API RESTful modularizada construida con **FastAPI**, implementando autenticación mediante **JSON Web Tokens (JWT)**, hashing seguro de contraseñas con **bcrypt** y **Control de Acceso Basado en Roles (RBAC)**.

---

## Características Principales

* **Seguridad & Autenticación:** 
  * Generación y validación de tokens Bearer JWT (`PyJWT`).
  * Encriptación de contraseñas mediante `bcrypt`.
* **Control de Acceso por Roles (RBAC):**
  * **Público:** Acceso libre a lecturas generales e individuales (`GET`).
  * **Cliente / Autenticado:** Creación, modificación de perfil y gestión de pedidos propios (`POST`, `PUT`).
  * **Administrador:** Control total sobre gestión de usuarios, eliminación de recursos y visualización global de pedidos (`DELETE`, `GET`).
* **Documentación Interactiva:** Integración automática con OpenAPI y Swagger UI en `/docs`.

---

## Estructura del Proyecto

```text
tienda-api/
├── routers/
│   ├── __init__.py
│   ├── auth.py          # Endpoints de login, registro y perfil
│   ├── categorias.py    # CRUD del módulo de Categorías
│   ├── pedidos.py       # CRUD del módulo de Pedidos
│   ├── productos.py     # CRUD del módulo de Productos
│   └── usuarios.py      # Administración de Usuarios y perfil
├── main.py              # Punto de entrada y orquestador de routers
├── seguridad.py         # Lógica JWT, bcrypt y dependencias RBAC
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación general

```


## 📌 Matriz de Endpoints y Permisos

### 🔑 Autenticación (`/auth`)

| Método | Endpoint | Descripción | Nivel de Acceso |
| --- | --- | --- | --- |
| `POST` | `/auth/login` | Inicia sesión y retorna Token JWT Bearer | Público |
| `POST` | `/auth/registro` | Registra un nuevo usuario con rol `cliente` | Público |
| `GET` | `/auth/yo` | Retorna la información del usuario autenticado | Autenticado |

### 📦 Productos (`/productos`)

| Método | Endpoint | Descripción | Nivel de Acceso |
| --- | --- | --- | --- |
| `GET` | `/productos` | Listar todos los productos | Público |
| `GET` | `/productos/{id}` | Consultar producto por ID | Público |
| `POST` | `/productos` | Crear un producto | Autenticado |
| `PUT` | `/productos/{id}` | Actualizar un producto existente | Autenticado |
| `DELETE` | `/productos/{id}` | Eliminar producto | **Admin** |

### 🏷️ Categorías (`/categorias`)

| Método | Endpoint | Descripción | Nivel de Acceso |
| --- | --- | --- | --- |
| `GET` | `/categorias` | Listar todas las categorías | Público |
| `GET` | `/categorias/{id}` | Consultar categoría por ID | Público |
| `POST` | `/categorias` | Crear una categoría | Autenticado |
| `PUT` | `/categorias/{id}` | Actualizar una categoría existente | Autenticado |
| `DELETE` | `/categorias/{id}` | Eliminar categoría | **Admin** |

### 👥 Usuarios (`/usuarios`)

| Método | Endpoint | Descripción | Nivel de Acceso |
| --- | --- | --- | --- |
| `GET` | `/usuarios` | Listar todos los usuarios | **Admin** |
| `GET` | `/usuarios/{username}` | Consultar usuario por username | **Admin** |
| `PUT` | `/usuarios/perfil` | Actualizar nombre del perfil actual | Autenticado |
| `DELETE` | `/usuarios/{username}` | Eliminar un usuario por username | **Admin** |

### 🛍️ Pedidos (`/pedidos`)

| Método | Endpoint | Descripción | Nivel de Acceso |
| --- | --- | --- | --- |
| `GET` | `/pedidos` | Listar pedidos (Cliente ve los suyos, Admin ve todos) | Autenticado |
| `GET` | `/pedidos/{id}` | Consultar pedido por ID (Dueño o Admin) | Autenticado |
| `POST` | `/pedidos` | Realizar un nuevo pedido | Autenticado |
| `DELETE` | `/pedidos/{id}` | Eliminar/Cancelar un pedido | **Admin** |

---

## 🛠️ Instalación y Ejecución

1. **Clonar el repositorio:**
```bash
git clone <URL_DE_TU_REPOSITO>
cd tienda-api

```


2. **Activar el entorno virtual:**
```bash
# Windows (PowerShell / CMD)
.\venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

```


3. **Instalar dependencias:**
```bash
pip install fastapi uvicorn pyjwt bcrypt pydantic

```


4. **Iniciar el servidor de desarrollo:**
```bash
uvicorn main:app --reload

```


5. **Acceder a la documentación interactiva:**
* **Swagger UI:** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)



```

---

### Pasos para guardar el README actualizado en GitHub:

Ejecuta estos 3 comandos desde la terminal de VS Code:

1. `git add README.md`
2. `git commit -m "Docs: Reorganizacion completa del README con modulos de Pedidos y Usuarios"`
3. `git push origin main` *(o `master` según el nombre de tu rama)*

```
