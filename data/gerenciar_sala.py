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
    print("=== Adicionar Sala ===")
    numeros = [int(s['numero']) for s in salas if s.get('numero').isdigit()]
    numero = str(max(numeros)+1) if numeros else "1"

    linhas = int(input("Quantidade de fileiras (linhas): ").strip())
    if any(l < 1 for l in [linhas]):
        print("❌ Quantidade de fileiras inválida.")
        return
    elif linhas > 10:
        print("⚠️  Atenção: fileiras acima de 10 podem não ser exibidas corretamente, digite um número menor.")
        return
    colunas = int(input("Poltronas por fileira (colunas): ").strip())
    if any(c < 1 for c in [colunas]):
        print("❌ Quantidade de poltronas inválida.")
        return
    elif colunas > 15:
        print("⚠️  Atenção: poltronas acima de 15 podem não ser exibidas corretamente, digite um número menor.")
        return
    salas.append({
        "numero": numero,
        "linhas": linhas,
        "colunas": colunas
    })
    salvar_salas(salas)
    print(f"> Sala {numero}: {linhas}×{colunas} adicionada.")



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
    for s in salas:
        total_cadeiras = s['linhas'] * s['colunas']
        print(f"• Sala {s['numero']} – {total_cadeiras} cadeiras")

def editar_sala():
    # resolver bugs...
    listar_salas()
    numero = input("Sala a editar: ").strip()
    for s in salas:
        if s["numero"] == numero:
            novo_cad = input(f"Novo total de linhas (atual {s['cadeiras']}): ").strip()
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

if __name__ == "__main__":
    gerenciar_salas()
