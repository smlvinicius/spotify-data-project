import requests
import time
from src.auth import get_token

# Sportify API base URL
BASE = "https://api.spotify.com/v1/"

# Função para obter headers com token de autenticação
def get_headers():
    token = get_token()
    return {
        "Authorization": f"Bearer {token}"}

# Função para fazer requisições GET a API do Spotify
def get_playlist_tracks(playlist_id, limit=100):
   
   # Extrair ID da playlist se for uma URL
    if "playlist" in playlist_id:
        playlist_id = playlist_id.rstrip("/").split("/")[-1].split("?")[0]

    headers = get_headers()
    url = f"{BASE}playlists/{playlist_id}/tracks"
    params = {"limit":limit, "offset":0}
    items = []
    




