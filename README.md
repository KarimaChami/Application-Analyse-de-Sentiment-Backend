# 
Application-Analyse-de-Sentimentproject/
│
├── sentiment-api/
│   ├── app/
│   │   ├── main.py
│   │   ├── sentiment.py
│   │   ├── auth.py          (optionnel)
│   │   ├── config.py
│   │   ├── schemas.py
│   │   └── __init__.py
│   │
│   ├── tests/
│   │   └── test_sentiment.py
│   │
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── pages/
│   │   ├── login/
│   │   │   └── page.tsx
│   │   ├── sentiment/
│   │   │   └── page.tsx
│   │   └── api/
│   │       └── sentiment/
│   │           └── route.ts
│   │
│   ├── components/
│   │   └── Navbar.tsx
│   │
│   ├── package.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md
