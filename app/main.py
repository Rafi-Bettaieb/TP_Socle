from fastapi import FastAPI
from data.data import users

app = FastAPI()

# Partie 2
@app.get("/")
def hello_fastapi() :
    return {"message" : "API FastAPI opérationnelle"}

# Partie 3
@app.get("/users")
def get_all_users():
    return users

# Partie 4.1 et 4.2
@app.get("/users/{user_id}")
def get_user_by_id(user_id:int) :
    return {"id" :user_id }

# Partie 4.3
@app.get("/search")
def search (name:str) :
    return {"search " : name}    