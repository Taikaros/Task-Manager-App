# Task Manager App

Una aplicación para gestionar tareas y recordatorios de manera fácil y eficiente. Permite a los usuarios registrarse, iniciar sesión y manejar sus tareas mediante una interfaz sencilla.

## Características

- **Registro de usuarios**: Los nuevos usuarios pueden registrarse para acceder a la aplicación.
- **Inicio de sesión**: Los usuarios pueden autenticarse con sus credenciales.
- **Gestión de tareas**:
  - Crear nuevas tareas.
  - Leer todas las tareas.
  - Leer una tarea específica por ID.
  - Actualizar tareas existentes.
  - Eliminar tareas.
- **Rehash de contraseñas**: Permite rehashar todas las contraseñas de usuarios existentes.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación.
- **FastAPI**: Framework web utilizado para construir la API.
- **SQLAlchemy**: ORM para gestionar la base de datos.
- **SQLite**: Base de datos utilizada (puedes cambiar esto a PostgreSQL u otra si es necesario).
- **Passlib**: Para el hashing y verificación de contraseñas.

## Requisitos

Antes de comenzar, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- pip

### Instalación

1. Clona el repositorio:
   ```bash  
   git clone https://github.com/tuusuario/tu-repo.git  
   cd tu-repo 
2. Crea un entorno virtual y activalo
    python -m venv venv
    # En Windows
    venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
3. Instala las dependencias
   pip install -r requeriments.txt

### Uso
    uvicorn app.main:app --reload
### Endpoints
    Aquí hay una lista de los endpoints disponibles en la aplicación:
    Registrar un nuevo usuario: POST /register
    Iniciar sesión: POST /login
    Crear una nueva tarea: POST /tasks/
    Leer todas las tareas: GET /tasks/
    Leer una tarea específica: GET /tasks/{task_id}
    Actualizar una tarea específica: PUT /tasks/{task_id}
    Eliminar una tarea específica: DELETE /tasks/{task_id}
    Rehash de contraseñas: POST /rehash_users