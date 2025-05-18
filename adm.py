def admInit():
    print("Olá, bem vindo ao sistema de gerenciamento de tickets.")
    print("Você está logado como Administrador.")
    admMenu()

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
            break
        elif opcao == "2":
            print("Gerenciando Filmes...")
            # add codigo
            break
        elif opcao == "3":
            print("Você escolheu Sair.")
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            opcao = input("Escolha uma opção (1, 2 ou 3): ")
            
