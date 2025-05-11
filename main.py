import adm
import vend
print("Tela de seleção de usuário")
print("1. Administrador")
print("2. Vendedor")
print("3. Sair")
opcao = input("Escolha uma opção (1, 2 ou 3): ")
while True:
    if opcao == "1":
        adm.admInit()
        break
    elif opcao == "2":
        vend.vendInit()
        break
    elif opcao == "3":
        print("Você escolheu Sair.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        opcao = input("Escolha uma opção (1, 2 ou 3): ")