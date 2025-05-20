import os
from data.gerenciar_sala import carregar_salas
from data.gerenciar_filmes import filmes as lista_filmes

def vendInit():
    print("Olá, bem-vindo ao sistema de gerenciamento de tickets.")
    print("Você está logado como Vendedor.\n")

    salas_list = carregar_salas()
    salas = {s['numero']: s for s in salas_list}

    while True:
        print("\nFilmes disponíveis:")
        for idx, f in enumerate(lista_filmes, start=1):
            print(f"  {idx} - {f['titulo']}")

        escolha = input("Escolha o número do filme: ").strip()
        if not escolha.isdigit() or not (1 <= int(escolha) <= len(lista_filmes)):
            print("Escolha inválida. Tente novamente.")
            continue

        filme_obj = lista_filmes[int(escolha) - 1]
        titulo    = filme_obj['titulo']
        salas_film= filme_obj.get('salas', [])

        if not salas_film:
            print(f"❌ O filme '{titulo}' não está atribuído a nenhuma sala.")
            continue

        print(f"\nSalas com '{titulo}':")
        for i, sn in enumerate(salas_film, start=1):
            sala_obj = salas.get(sn)
            cadeiras = sala_obj['cadeiras'] if sala_obj else "??"
            print(f"  {i} - Sala {sn} ({cadeiras} cadeiras)")

        escolha_sala = input("Escolha o número da sala: ").strip()
        if not escolha_sala.isdigit() or not (1 <= int(escolha_sala) <= len(salas_film)):
            print("Opção de sala inválida.")
            continue

        sala_num = salas_film[int(escolha_sala) - 1]
        sala_obj = salas.get(sala_num)
        if not sala_obj:
            print(f"❌ Sala {sala_num} não encontrada.")
            continue

        print(f"\nFilme selecionado: {titulo}")
        print(f"Sala escolhida: {sala_num} ({sala_obj['cadeiras']} cadeiras)")
        confirmar = input("Digite '1' para confirmar a venda ou qualquer outra tecla para cancelar: ").strip()
        if confirmar != "1":
            print("Operação cancelada.")
            continue

        print(f"\n✅ Ingresso vendido para '{titulo}' na sala {sala_num}.")

        if input("\nDeseja vender outro ingresso? (s/n): ").strip().lower() != "s":
            print("\nVendas Fechadas.")
            break

if __name__ == "__main__":
    vendInit()
