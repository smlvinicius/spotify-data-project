import requests
import base64
import json
import os

def get_token(credentials_path="config/credentials.json"):
    # 1) ler arquivo de credenciais
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"Credenciais não encontradas em: {credentials_path}")

    with open(credentials_path, "r", encoding="utf-8") as f:
        creds = json.load(f)

    client_id = creds.get("client_id")
    client_secret = creds.get("client_secret")

    if not client_id or not client_secret:
        raise ValueError("client_id ou client_secret ausentes no arquivo de credenciais.")

    # 2) montar header de Basic Auth (base64)
    auth_str = f"{client_id}:{client_secret}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {b64_auth}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    # 3) requisitar token
    response = requests.post(url, headers=headers, data=data)

    # 4) checar erro
    if response.status_code != 200:
        # para debug: exibir resposta completa
        raise Exception(f"Erro ao obter token (status {response.status_code}): {response.text}")

    token = response.json().get("access_token")
    if not token:
        raise Exception("Resposta não contém access_token.")

    return token
