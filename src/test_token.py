from src.auth import get_token

if __name__ == "__main__":
    token = get_token()
    print("Token obtido com sucesso:")
    print(token)
