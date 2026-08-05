Tienda API - Módulo FastAPI CRUD

API RESTful modular construida con **FastAPI** y **Python** para la gestión de productos y categorías. Desarrollada como evidencia de laboratorio para la arquitectura de aplicaciones web con validación de datos mediante **Pydantic**.



## Características

* **Arquitectura Modular:** Separación clara de rutas por dominio utilizando `APIRouter`.
* **CRUD Completo:** Operaciones de Creación, Lectura, Actualización y Eliminación para recursos de *Categorías* y *Productos*.
* **Validación de Datos:** Uso estricto de esquemas `Pydantic` (`BaseModel`) para validar los tipos de datos de entrada y salida.
* **Manejo de Errores:** Respuestas HTTP estandarizadas (`404 Not Found`, `422 Unprocessable Entity`).
* **Documentación Automática:** Swagger UI y ReDoc integrados nativamente.

---

## Estructura del Proyecto

```text
Tienda-Api/
│
├── routers/
│   ├── __init__.py
│   ├── categorias.py    # Endpoints para el recurso Categorías
│   └── productos.py     # Endpoints para el recurso Productos
│
├── .gitignore           # Exclusión de venv y archivos temporales
├── main.py              # Punto de entrada de la aplicación FastAPI
└── README.md            # Documentación del proyecto
```


 ### Requisitos PreviosPython
 3.10 o superiorGit
 
### Instalación y Configuración

Clonar el repositorio:Bashgit clone [https://github.com/liney042-alt/Tienda-Api.git]

cd Tienda-Api
Crear y activar el entorno virtual:En Windows (PowerShell):PowerShellpython -m venv venv
.\venv\Scripts\activate
En Linux/macOS:Bashpython3 -m venv venv
source venv/bin/activate
Instalar dependencias:Bashpip install fastapi uvicorn pydantic

### Ejecución del ServidorPara iniciar el servidor de desarrollo en modo recarga automática (hot-reload):Bashuvicorn main:app --reload
El servicio estará disponible en: http://127.0.0.1:8000

### Pruebas y Documentación

 InteractivaFastAPI genera documentación interactiva automáticamente. Puedes probar todos los endpoints del CRUD directamente en el navegador:Swagger UI: http://127.0.0.1:8000/docsReDoc: http://127.0.0.1:8000/redoc
 
