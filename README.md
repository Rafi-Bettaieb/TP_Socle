# Partie 1 :
## Question 1 :
création du projet

## Question 2 :
création de l'environnement virtuel
```bash
python3 -m venv .venv
```
activation de l'environnement virtuel
```bash 
source .venv/bin/activate
```
## Question 3 :
```bash
pip install fastapi uvicorn pydantic
```
FastAPI : C'est le framework qui construit l'application et gère sa logique.
Uvicorn : C'est le serveur qui connecte l'application au réseau pour la rendre accessible.
Pydantic : C'est le validateur qui vérifie que les données reçues sont correctes avant de les utiliser.

## Question 4 :
geler la configuration dans le fichier
```bash 
pip freeze > requirements-dev.txt
```
---

# Partie 2 :
## Question 1 :
création du fichier main.py

## Question 2 :
lancer l'application
```bash
uvicorn main:app
```

## Question 3 :
accédr àl'API et le tester avec swagger

URL : http://127.0.0.1:8000/
Swagger : http://127.0.0.1:8000/docs#/default/hello_fastapi__get

# Partie 3 :
# Question 1 :
creation du dictionnaire
creation de ficiher data.py pour stocker les données

# Question 2 :
from data import users
GET /users -> return users

test avec Swagger
http://127.0.0.1:8000/docs#/default/get_all_users_users_get

# Partie 4 :
# 4.1
fonction de get_user_by_id selon l'id dans l'URL

# 4.2
Cas 1 : GET /users/1
1- la route est executée
2- la valeur retournée est {"id":1} 

Cas 2 : GET /users/toto

1- la fonction n'est pas exécutée
le code HTTP retourné est : 422
le paramétre concerné est user_id
le type attendu est int et non pas str

# 4.3
GET /search -> {"detail":[{"type":"missing","loc":["query","name"],"msg":"Field required","input":null}]}
GET /search?name=alice -> {"search ":"alice"}
GET /search?name=123 -> {"search ":"123"}

1- le paramétre est obligatoir
2- "alice" est bien du texte. 
FastAPI lit et transforme automatiquement en texte ("123"). Comme "123" est un texte valide.