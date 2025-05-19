import os
def admInit():
    clear_screen()
    print("Olá, bem vindo ao sistema de gerenciamento de tickets.")
    print("Você está logado como Administrador.")
    admMenu()
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def admMenu():
    print("=== Menu do Administrador ===")
    print("1. Gerenciar Salas")
    print("2. Gerenciar Filmes")
    print("3. Sair")
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    while True:
        if opcao == "1":
            print("Gerenciando Salas...")
            import data.gerenciar_sala as gerenciar_sala
            gerenciar_sala.gerenciar_salas()
        elif opcao == "2":
            print("Gerenciando Filmes...")
            import data.gerenciar_filmes as gerenciar_filmes
            gerenciar_filmes.gerenciar_filmes()
        elif opcao == "3":
            print("Você escolheu Sair.")
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            opcao = input("Escolha uma opção (1, 2 ou 3): ")
            
# admInit()