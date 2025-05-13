import json
import os
USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        print(f"Arquivo '{USERS_FILE}' não encontrado.")
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def login(tipoUsuario):
    users = load_users()
    if not users:
        return

    while True:
        print("=== Sistema de Login ===")
        username = input("Usuário: ")
        password = input("Senha: ")

        if not username.strip() or not password.strip():
            print("Erro: Campos de usuário e senha não podem estar vazios.")
            continue

        if username in users and users[username] == password:
            print("Login bem-sucedido!")
            if tipoUsuario == "adm":
                import adm
                adm.admInit()
            elif tipoUsuario == "vend":
                import vend
                vend.vendInit()
            break
        else:
            print("Usuário ou senha incorretos. Tente novamente.")

if __name__ == "__main__":
    login()
