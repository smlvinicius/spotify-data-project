import requests
import time
from src.auth import get_token

# Sportify API base URL
BASE = "https://api.spotify.com/v1/"

# Função para obter headers com token de autenticação
def get_headers():
    token = get_token()
    return {"Authorization": f"Bearer {token}"}

# Função para fazer requisições GET a API do Spotify
def get_playlist_tracks(playlist_id, limit=100):
    # Extrair ID da playlist se for uma URL
    if "playlist" in playlist_id:
        playlist_id = playlist_id.rstrip("/").split("/")[-1].split("?")[0]

    headers = get_headers()
    url = f"{BASE}playlists/{playlist_id}/tracks"
    params = {"limit": limit, "offset": 0}
    items = []

    # Loop para paginar através dos resultados
    while True:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        items.extend(data.get("items", []))

        if data.get("next") is None:
            break

        params["offset"] += limit
        time.sleep(0.1)  # Pequena pausa para evitar rate limiting

    return items

def get_audio_features(track_ids):
    headers = get_headers()
    features = []
    # Batch de 100 IDs por requisição
    batch_size = 100
    for i in range(0, len(track_ids), batch_size):
        batch_ids = track_ids[i:i + batch_size]
        ids_param = ",".join(batch_ids)
        url = f"{BASE}audio-features"
        params = {"ids": ids_param}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        features.extend(data.get("audio_features", []))
        time.sleep(0.1)  # Pequena pausa para evitar rate limiting
    return features

def get_track_info(track_ids):
    headers = get_headers()
    tracks = []
    # Batch de 50 IDs por requisição
    batch_size = 50
    for i in range(0, len(track_ids), batch_size):
        batch_ids = track_ids[i:i + batch_size]
        ids_param = ",".join(batch_ids)
        url = f"{BASE}tracks"
        params = {"ids": ids_param}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json()
        tracks.extend(data.get("tracks", []))
        time.sleep(0.1)  # Pequena pausa para evitar rate limiting
    return tracks









