from fastapi import FastAPI
from sqlmodel import SQLModel
from fastapi import FastAPI, HTTPException

app = FastAPI()

class User(SQLModel):
    id: int | None = None
    username: str
    password: str
    email: str | None = None
    is_active: bool = True

class UserUpdate(SQLModel):
    username: str | None = None
    email: str | None = None
    is_active: bool | None = None

db_users = [
    User(id=1, username="admin", password="admin", email="admin@test.com"),
    User(id=2, username="user", password="user", email=""),
    User(id=3, username="guest", password="guest", email="guest@test.com"),
]

next_id = 4

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login(user: User):
    for db_user in db_users:
        if db_user.username == user.username and db_user.password == user.password:
            return {"message": "Entraste!!"}
    raise HTTPException(status_code=401, detail="Usuario y contraseña no encontradas")

@app.post("/users")
def create_user(user: User):
    global next_id
    for db_user in db_users:
        if db_user.username == user.username:
            return {"message": "Username ya existe"}
    user.id = next_id
    next_id += 1
    db_users.append(user)
    return {"message": "Usuario creado", "id": user.id, "username": user.username}

@app.get("/users")
def list_users():
    return [{"id": u.id, "username": u.username, "email": u.email, "is_active": u.is_active} for u in db_users]

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for u in db_users:
        if u.id == user_id:
            return {"id": u.id, "username": u.username, "email": u.email, "is_active": u.is_active}
    return {"message": "Usuario no encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, data: UserUpdate):
    for u in db_users:
        if u.id == user_id:
            if data.username is not None:
                u.username = data.username
            if data.email is not None:
                u.email = data.email
            if data.is_active is not None:
                u.is_active = data.is_active
            return {"message": "Usuario actualizado", "id": u.id, "username": u.username}
    return {"message": "Usuario no encontrado"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, u in enumerate(db_users):
        if u.id == user_id:
            db_users.pop(i)
            return {"message": "Usuario eliminado", "username": u.username}
    return {"message": "Usuario no encontrado"}

