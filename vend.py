import json
import os

SALAS = "salas.json"
FILMES = "filmes.json"
ASSENTOS= "assentos.json"

def carregar_dados(arquivo, padrao):
    if not os.path.exists(arquivo):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(padrao, f)
        return padrao
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2)

def vendInit():
    print("Olá, bem vindo ao sistema de gerenciamento de tickets.")
    print("Você está logado como Vendedor.", end = '\n\n')

    salas = carregar_dados(SALAS, {"1": "Sala 1", "2": "Sala 2"})
    filmes = carregar_dados(FILMES, {"1": "Oppenheimer", "2": "Barbie"})
    assentos = carregar_dados(ASSENTOS, {
        "1": [["01","02","03"],["04","05","06"]],
        "2": [["01","02","03"],["04","05","06"]]
    })

    while True:
        print("\nSalas disponíveis:")
        for k, v in salas.items():
            print(f"{k} - {v}")
        sala = input("Escolha o número da sala: ").strip()
        if sala not in salas:
            print("Sala inválida.")
            continue

        print("\nFilmes disponíveis nesta sala:")
        print(f"1 - {filmes[sala]}")
        filme_escolhido = input("Digite o nome do filme: ").strip()
        if filme_escolhido.lower() != filmes[sala].lower():
            print("Filme não está em exibição nesta sala.")
            continue

        print("\nMapa de assentos (xx = ocupado):")
        for i, linha in enumerate(assentos[sala]):
            print(" ".join(linha))
        assento = input("Escolha o número do assento: ").zfill(2)
        ocupado = False
        for i, linha in enumerate(assentos[sala]):
            for j, val in enumerate(linha):
                if val == assento:
                    assentos[sala][i][j] = "xx"
                    ocupado = False
                    break
                elif val == "xx" and assento == val:
                    ocupado = True
            if ocupado:
                break
        if ocupado:
            print("Assento já ocupado. Tente novamente.")
            continue
        else:
            print(f"Ingresso vendido para o filme '{filmes[sala]}' na sala {sala}, assento {assento}.")
            salvar_dados(ASSENTOS, assentos)

        if input("Deseja vender outro ingresso? (s/n): ").lower() != "s":
            print('Vendas Fechadas.')
            break

<<<<<<< HEAD
vendInit()
=======
vendInit()
>>>>>>> 6c1a076e61b2ee23a0459492474ac5af8d590573
