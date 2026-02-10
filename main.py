from fastapi import FastAPI
from data import users

app = FastAPI()

# Partie 2
@app.get("/")
def hello_fastapi() :
    return {"message" : "API FastAPI opérationnelle"}

# Partie 3
@app.get("/users")
def get_all_users():
    return users