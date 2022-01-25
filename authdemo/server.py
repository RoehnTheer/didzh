# Сервак на фастапи
import base64
import hmac
import hashlib
import json
from typing import Optional
from fastapi import FastAPI, Form, Cookie, Body
from fastapi.responses import Response

app = FastAPI()

SECRET_KEY = "9d046dc3eba89c2f99ecf781682e873cfe11bee3b4fda711c3694bc601e9b90d"
PASSWORD_SALT = "7f655300f26397a4cbf98fe89c0d4749b099bce9c2be9a43ae3c0601be8f5de0"

users = {
    "theer@mail.ru": {
        "name": "Misha",
        "password": "86fa43826527b81b12eb07aa54f83df6c75046c1f20a691dfb8006173a452daf"
    }
}


def sign_data(data: str) -> str:
    return hmac.new(
        SECRET_KEY.encode(),
        msg=data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest().upper()


def get_username_from_signed_string(username_signed: str) -> Optional[str]:
    username_base64, sign = username_signed.split(".")
    username = base64.b64decode(username_signed.encode()).decode()
    valid_sign = sign_data(username)
    if hmac.compare_digest(valid_sign, sign):
        return username


def verify_password(username: str, password: str) -> bool:
    password_hash = hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower()
    stored_password_hash = users[username]["password"].lower()
    return password_hash == stored_password_hash


@app.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/login.html", "r") as f:
        login_page = f.read()
    if not username:
        return Response(login_page, media_type="text/html")
    valid_username = get_username_from_signed_string(username)
    if not valid_username:
        responce = Response(login_page, media_type="text/html")
        responce.delete_cookie(key="username")
        return responce
    try:
        user = users[valid_username]
    except KeyError:
        user = users[valid_username]
        responce = Response(login_page, media_type="text/html")
        responce.delete_cookie(key="username")
        return responce
    return Response(f"Helloooo, {users[valid_username]['name']}!!!!!", media_type="text/html")


@app.post("/login")
def process_login_page(data: dict = Body(...)):
    print("Датка из ", data)
    username = data["username"]
    password = data["password"]
    user = users.get(username)
    if not user or not verify_password(username, password):
        return Response(
            json.dumps({
                "success": False,
                "message": "ТЫ КТОАА?"
            }),
            media_type="application/json")
    responce = Response(
        json.dumps({
            "success": True,
            "message": f"Привет, {user['name']}"
        }),
        media_type="application/json")
    user_signed = base64.b64encode(username.encode()).decode() + "." + sign_data(username)
    responce.set_cookie(key="username", value=user_signed)
    return responce
