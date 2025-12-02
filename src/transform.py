import pandas as pd

# Função para receber uma lista de itens da playlist e retornar um DataFrame estruturado
def parse_playlist_items(items):

  rows = []
  for item in items:
      # Algumas faixas podem não estar disponiveis e ter o valor None, por isso fazemos essa verificação
      track = item.get("track", {})
      if track is None:
          continue
      