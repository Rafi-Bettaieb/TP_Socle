# TP1_a

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

---

# Partie 3 :
# Question 1 :
creation du dictionnaire
creation de ficiher data.py pour stocker les données

# Question 2 :
from data import users
GET /users -> return users

test avec Swagger
http://127.0.0.1:8000/docs#/default/get_all_users_users_get

---

# Partie 4 :
## 4.1
fonction de get_user_by_id selon l'id dans l'URL

## 4.2
Cas 1 : GET /users/1
1- la route est executée
2- la valeur retournée est {"id":1} 

Cas 2 : GET /users/toto

1- la fonction n'est pas exécutée
le code HTTP retourné est : 422
le paramétre concerné est user_id
le type attendu est int et non pas str

## 4.3
GET /search -> {"detail":[{"type":"missing","loc":["query","name"],"msg":"Field required","input":null}]}

GET /search?name=alice -> {"search ":"alice"}

GET /search?name=123 -> {"search ":"123"}

1- le paramétre est obligatoir
2- "alice" est bien du texte. 
FastAPI lit et transforme automatiquement en texte ("123"). Comme "123" est un texte valide.

---

# Partie 5 :
## 5.1
### Question 1 :
l'utilisateur ne doit pas choisir son propre numéro.

### Question 2 :
par qui : par la base de données (le système de stockage).
quand : automatiquement au moment où l'utilisateur est sauvegardé.

## 5.2
creation des fichiers user_model_create.py et user_model.py

### Question 1 :
Pour différencier les données d'Entrée (ce que l'utilisateur envoie) des données de Sortie (ce que l'API renvoie, qui inclut l'ID).

### Question 2 :
Parce que l'utilisateur n'a pas encore d'ID au moment où il s'inscrit.

### Question 3 :
Par la Base de Données, au moment précis de l'enregistrement.

### Question 4 :
L'API refuserait toutes les inscriptions car l'utilisateur ne peut pas fournir l'id lui meme.

### Question 5 :
l'heritage est évite pour previligier la lisibilite et la meilleur comprehension du role de chaque modéle.

## 5.3 + 5.4
#### Question 1 :
pour séparer la logique métier de la logique web.

### Question 2 :
il sera difficile ou impossible de tester le code sans utiliser le serveur web

### Question 3 :
pour importer des données.

## 5.5 :

creation des tests pour verifier :
la longueur des utilisateurs chargés / id / login / age de l'utilisateur

Mise à jour de l'arborescence

---

# Partie 6 :
## Etape 1 + 2
Modification de la structure du projet

## Etape 3 :
création du fichier settings.py

## Etape 4 :
### Question 1 :
```bash
pip install python-dotenv
```
### Question 2 :
```bash
pip freeze > requirements-dev.txt
```
## Etape 5 :
implementation de la classe Settings

## Etape 6 :
Ecriture des tests