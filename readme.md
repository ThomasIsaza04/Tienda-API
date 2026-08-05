# Tienda API — Sistema de Gestión y Seguridad con FastAPI

> **API RESTful profesional y modular construida con FastAPI, Python y Pydantic.**  
> Diseñada bajo principios de arquitectura limpia, validación de datos estricta y control de acceso basado en roles (RBAC) mediante JWT.

---

## Descripción General

**Tienda API** es una solución backend diseñada para gestionar el catálogo completo de un sistema de comercio electrónico (categorías, productos) e incorporar mecanismos de autenticación y autorización segura. 

Este proyecto implementa las mejores prácticas de desarrollo en Python:
* **Inyección de dependencias** nativa de FastAPI.
* **Mapeo y validación de esquemas** con Pydantic v2.
* **Seguridad y JWT** para protección de rutas críticas.
* **Estructura modular reutilizable** y escalable.

---

## Características Principales

- **Autenticación & Seguridad:**
  - Encriptación de contraseñas.
  - Generación y validación de tokens Bearer JWT (`OAuth2PasswordBearer`).
  - Control de acceso por roles (p. ej., restricción de rutas exclusivas para administradores).

- **Módulo de Productos & Categorías:**
  - Operaciones **CRUD complejas** (Create, Read, Update, Delete).
  - Paginación y filtrado de catálogo.
  - Validación de tipos de datos e integridad referencial lógica.

- **Arquitectura & Calidad:**
  - Separación de responsabilidades mediante `APIRouter`.
  - Tratamiento centralizado de excepciones HTTP (`401 Unauthorized`, `403 Forbidden`, `404 Not Found`).
  - Generación de esquemas Open-API 3.0 en tiempo de ejecución.

---

## Estructura del Proyecto

```text
Tienda-Api/
│
├── routers/
│   ├── __init__.py
│   ├── auth.py          # Autenticación, inicio de sesión y emisión de tokens
│   ├── categorias.py    # Endpoints para el recurso Categorías
│   ├── productos.py     # Endpoints para el recurso Productos
│   └── seguridad.py     # Funciones de utilería JWT, hashing y dependencias
│
├── .gitignore           # Exclusión de venv, variables de entorno y temporales
├── main.py              # Punto de entrada y configuración global del servidor
└── README.md            # Documentación del proyecto

```

---

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
* **Servidor ASGI:** [Uvicorn](https://www.google.com/search?q=https://www.uvicorn.org/)
* **Validación de Datos:** [Pydantic v2](https://www.google.com/search?q=https://docs.pydantic.dev/)
* **Seguridad:** PyJWT / Passlib / OAuth2

---

## Requisitos Previos

Antes de comenzar, asegúrate de contar con lo siguiente instalado en tu equipo:

* **Python 3.10** o superior.
* **Git** para el control de versiones.
* Un gestor de paquetes (`pip`).

---

## Instalación y Configuración

1. **Clonar el repositorio:**
```bash
git clone [https://github.com/ThomasIsaza04/Tienda-API.git](https://github.com/ThomasIsaza04/Tienda-API.git)
cd Tienda-Api

```


2. **Crear y activar un entorno virtual:**
* En **Windows (PowerShell / CMD):**
```powershell
python -m venv venv
.\venv\Scripts\activate

```


* En **Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate

```




3. **Instalar las dependencias del proyecto:**
```bash
pip install fastapi uvicorn pydantic pyjwt "passlib[bcrypt]"

```



---

## Ejecución del Servidor

Para iniciar el servidor en modo de desarrollo con recarga automática (*hot-reload*):

```bash
uvicorn main:app --reload

```

El servicio estará disponible de manera predeterminada en:
**`http://127.0.0.1:8000`**

---

## Endpoints Principales

### Autenticación & Seguridad

| Método | Endpoint | Descripción | Requiere Auth |
| --- | --- | --- | --- |
| `POST` | `/auth/login` | Autentica un usuario y devuelve un token JWT | ❌ |
| `GET` | `/auth/me` | Obtiene el perfil del usuario autenticado | Bearer |

### Categorías

| Método | Endpoint | Descripción | Requiere Auth |
| --- | --- | --- | --- |
| `GET` | `/categorias/` | Lista todas las categorías | ❌ |
| `POST` | `/categorias/` | Crea una nueva categoría | 🔒 Admin |
| `PUT` | `/categorias/{id}` | Actualiza una categoría existente | 🔒 Admin |
| `DELETE` | `/categorias/{id}` | Elimina una categoría | 🔒 Admin |

### Productos

| Método | Endpoint | Descripción | Requiere Auth |
| --- | --- | --- | --- |
| `GET` | `/productos/` | Lista los productos en catálogo | ❌ |
| `GET` | `/productos/{id}` | Obtiene el detalle de un producto específico | ❌ |
| `POST` | `/productos/` | Agrega un nuevo producto al inventario | 🔒 Admin |
| `PUT` | `/productos/{id}` | Modifica la información de un producto | 🔒 Admin |
| `DELETE` | `/productos/{id}` | Remueve un producto | 🔒 Admin |

---

## Documentación Interactiva

FastAPI genera documentación interactiva en vivo sin necesidad de herramientas externas:

* **Swagger UI (Pruebas interactivas):** [http://127.0.0.1:8000/docs](https://www.google.com/search?q=http://127.0.0.1:8000/docs)
* **ReDoc (Especificación limpia):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

> **Tip:** Desde **Swagger UI** puedes usar el botón **"Authorize"** e ingresar tu token JWT (`Bearer <tu_token>`) para probar los endpoints protegidos.

---

## Autor

Desarrollado por **Thomas Isaza Chalarca** — [ThomasIsaza04](https://www.google.com/search?q=https://github.com/ThomasIsaza04)

```

<FollowUp label="¿Quieres que le agregue algún módulo específico o guía de testing?" query="¿Puedes actualizar el README para agregar una sección de pruebas unitarias con Pytest?"/>

```