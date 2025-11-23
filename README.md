# 🧠 Micro-Service d’Analyse de Sentiment — Backend (FastAPI)

## 📌 Contexte du projet
L’agence souhaite automatiser l’analyse des avis clients provenant des réseaux sociaux, formulaires de satisfaction et plateformes e-commerce.  
Faute de temps pour entraîner un modèle NLP, l’entreprise utilise l’API Hugging Face Inference avec le modèle :

- **Modèle :** `nlptown/bert-base-multilingual-uncased-sentiment`
- **Sortie :** score entre **1 et 5**

## 🎯 Objectif du backend
Créer une API FastAPI sécurisée par **JWT** qui :
- reçoit un texte,
- appelle Hugging Face Inference API,
- renvoie un score + sentiment (`negatif`, `neutre`, `positif`),
- protège l’accès via JWT,
- soit dockerisable,
- soit testée (Pytest + Postman).

---

## 📁 Structure du projet

Application-Analyse-de-Sentimentproject/
│
├── sentiment-api/
│   ├── app/
│        ├── database/
│           ├── config.py
│           ├── db.py          
│           ├── models.py
│           └── schemas.py
│        ├── auth.py          
│        ├── Dockerfile
│        ├── main.py
│        ├── sentiment.py
│        │
│        ├── tests/
│            └── test_predict.py
│        
├── docker-compose.yml
├── requirements.txt
└── README.md



---

## 🔐 Variables d’environnement (.env)


```env
HUGGINGFACE_API_KEY=your_huggingface_api_key
JWT_SECRET_KEY=your_jwt_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./sentiment.db
``` 
---

---

## 🚀 Endpoints de l’API

### **POST /login**
Authentifie un utilisateur et génère un JWT.

**Exemple de requête :**
```json
{
  "username": "kima",
  "password": "password123"
}

```
**Réponse :
```json
{
  "access_token": "<jwt>",
  "token_type": "bearer"
}
```
## **POST /predict**

📌 Endpoint protégé (JWT obligatoire)

Reçoit un texte → envoie à HuggingFace → renvoie score + sentiment.
**Exemple de requête :**
```json
{
  "text": "J'adore ce produit !"
}
```
**Réponse :**
```json
{
  "score": 5,
  "sentiment": "positif"
}
```

---
## 🧪 Tests
- **Pytest** : tests unitaires pour la logique de prédiction.
- **Postman** : collection pour tester les endpoints API.
- **Docker** : conteneurisation de l’application pour un déploiement facile.
---
## 📦 Dockerisation
- **Dockerfile** : pour construire l’image de l’application FastAPI.
- **docker-compose.yml** : pour orchestrer les services (API + base de données).
---
## 🧰 Lancement en mode développement
1. Cloner le dépôt :
   ```bash
   git clone <repository_url>
   cd Application-Analyse-de-Sentimentproject/sentiment-api
   ```
2. pip install -r requirements.txt
3. Lancer l’application :
   ```bash
   uvicorn app.main:app --reload
   ```
