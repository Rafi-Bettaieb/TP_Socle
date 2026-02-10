# Partie 1 :
## question 1 :
création du projet

## question 2 :
création de l'environnement virtuel
```bash
python3 -m venv .venv
```
activation de l'environnement virtuel
```bash 
source .venv/bin/activate
```
## question 3 :
```bash
pip install fastapi uvicorn pydantic
```
FastAPI : C'est le framework qui construit l'application et gère sa logique.
Uvicorn : C'est le serveur qui connecte l'application au réseau pour la rendre accessible.
Pydantic : C'est le validateur qui vérifie que les données reçues sont correctes avant de les utiliser.

## question 4 :
geler la configuration dans le fichier
```bash 
pip freeze > requirements.txt
```
