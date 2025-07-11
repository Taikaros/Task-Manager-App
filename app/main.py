from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, get_db, Base
from .models import UserModel
from . import auth
from .schemas import UserCreate  # Importa el modelo Pydantic para validar la entrada
from .routes import router as api_router
# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Inicializar la aplicación FastAPI
app = FastAPI()

# Ruta raíz de la aplicación
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Ruta para registrar un nuevo usuario
@app.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    
    # Crear y agregar el nuevo usuario en el modelo UserModel
    new_user = UserModel(username=user.username, hashed_password=user.password)  # Cambia esto hacia tu método de hash
    db.add(new_user)
    db.commit()
    db.refresh(new_user)  # Obtiene los datos más recientes del nuevo usuario

    # Retornar el usuario creado
    return {"username": new_user.username}

# Incluir las rutas
app.include_router(api_router)