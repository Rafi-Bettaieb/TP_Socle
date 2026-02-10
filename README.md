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