from datetime import datetime, timedelta
from fastapi import Request, HTTPException,Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.database.config import settings
# --- Fake user database ---
fake_users = {
    "kima": "password123"
}

# --- Create JWT token ---
def create_access_token(username: str):
    to_encode = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt

# --- Verify JWT token manually ---
security = HTTPBearer() #FastAPI automatically adds the 🔑 Authorize button in /docs
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials  # <-- this is the JWT token
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return username
    except JWTError:
        raise HTTPException(status_code=403, detail="Token expired or invalid")
# --- Authenticate user ---
def authenticate_user(username: str, password: str):
    return username in fake_users and fake_users[username] == password
