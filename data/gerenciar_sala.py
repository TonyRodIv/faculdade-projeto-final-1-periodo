import json
import os

ARQUIVO_SALAS = os.path.join('data', 'temp', 'salas.json')

def garantir_pasta():
    pasta = os.path.dirname(ARQUIVO_SALAS)
    os.makedirs(pasta, exist_ok=True)

def carregar_salas():
    garantir_pasta()
    if os.path.exists(ARQUIVO_SALAS):
        with open(ARQUIVO_SALAS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_salas(salas):
    """Salva a lista de salas no arquivo JSON."""
    garantir_pasta()
    with open(ARQUIVO_SALAS, 'w', encoding='utf-8') as f:
        json.dump(salas, f, ensure_ascii=False, indent=4) 

salas = carregar_salas()

def adicionar_sala():
    numeros_existentes = []
    for s in salas:
        try:
            numeros_existentes.append(int(s['numero']))
        except (KeyError, ValueError):
            pass
    if numeros_existentes:
        proximo_numero = max(numeros_existentes) + 1
    else:
        proximo_numero = 1

    numero_str = str(proximo_numero)
    print(f"> Número da sala atribuído automaticamente: {numero_str}")
    cadeiras = int(input("Número de cadeiras: ").strip())
    salas.append({"numero": numero_str, "cadeiras": cadeiras})
    salvar_salas(salas)
    print(f"> Sala {numero_str} com {cadeiras} cadeiras adicionada.")



def remover_sala():
    numero = input("Número da sala a remover: ").strip()
    antes = len(salas)
    salas[:] = [s for s in salas if s["numero"] != numero]
    if len(salas) < antes:
        salvar_salas(salas)
        print(f"> Sala {numero} removida.")
    else:
        print(f"> Sala {numero} não encontrada.")

def listar_salas():
    if not salas:
        print("> Nenhuma sala cadastrada.")
    else:
        for s in salas:
            print(f"• Sala {s['numero']} – {s['cadeiras']} cadeiras")

def editar_sala():
    numero = input("Sala a editar: ").strip()
    for s in salas:
        if s["numero"] == numero:
            novo_cad = input(f"Novo total de cadeiras (atual {s['cadeiras']}): ").strip()
            if novo_cad:
                s["cadeiras"] = int(novo_cad)
            salvar_salas(salas)
            print(f"> Sala atualizada para {numero} – {s['cadeiras']} cadeiras.")
            return
    print(f"> Sala {numero} não encontrada.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerenciar_salas():
    while True:
        clear_screen()
        print("=== Gerenciar Salas ===")
        print("1. Adicionar Sala")
        print("2. Remover Sala")
        print("3. Listar Salas")
        print("4. Editar Sala")
        print("5. Voltar")
        opc = input("Opção (1–5): ").strip()

        if opc == "1":
            adicionar_sala()
        elif opc == "2":
            remover_sala()
        elif opc == "3":
            listar_salas()
        elif opc == "4":
            editar_sala()
        elif opc == "5":
            import adm
            adm.admInit()
        else:
            print("> Opção inválida.")
        input("\nEnter para continuar...")

# if __name__ == "__main__":
#     gerenciar_salas()
