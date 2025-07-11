from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, auth, schemas
from .database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Registrarse
@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(models.UserModel).filter(models.UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    # Guardar la contraseña en texto plano
    new_user = models.UserModel(username=user.username, hashed_password=user.password)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al crear el usuario")
    
    return {"username": new_user.username}

# Iniciar sesión
@router.post("/login", response_model=schemas.UserResponse)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.UserModel).filter(models.UserModel.username == user.username).first()
    if not db_user or db_user.hashed_password != user.password:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    return {"username": db_user.username}

# Crear una nueva tarea
@router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    new_task = models.TaskModel(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

# Leer todas las tareas
@router.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(models.TaskModel).offset(skip).limit(limit).all()
    return tasks

# Leer una tarea por ID
@router.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

# Actualizar una tarea
@router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    existing_task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    existing_task.title = task.title
    existing_task.description = task.description
    db.commit()
    db.refresh(existing_task)
    return existing_task

# Eliminar una tarea
@router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.TaskModel).filter(models.TaskModel.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(task)
    db.commit()
    return task