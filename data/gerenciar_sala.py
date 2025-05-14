import os

def gerenciar_salas():
    # para contexto, esse é um sistema de bilheteria de cinema
    print("=== Gerenciar Salas ===")
    print("1. Adicionar Sala")
    print("2. Remover Sala")
    print("3. Listar Salas")
    print("4. Editar Sala")
    print("5. Voltar")
    opcao = input("Escolha uma opção (1, 2, 3, 4 ou 5): ")
    
    while True:
        if opcao == "1":
            adicionar_sala()
        # elif opcao == "2":
        #     remover_sala()
        # elif opcao == "3":
        #     listar_salas()
        # elif opcao == "4":
        #     editar_sala()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")
            
def adicionar_sala():
    print("=== Adicionar Sala ===")
    sala = input("Digite o número da sala: ")
    num_cadeiras = input("Digite o número de cadeiras disponíveis: ")
    
    with open(f"data/temp/sala_{sala}.txt", "w") as f:
        f.write(num_cadeiras)
    
    print(f"Sala {sala} adicionada com {num_cadeiras} cadeiras disponíveis.")