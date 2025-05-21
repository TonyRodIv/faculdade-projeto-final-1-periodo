import os
from data.gerenciar_sala import carregar_salas
from data.gerenciar_filmes import filmes as lista_filmes
from data.gerenciar_assentos import (
    carregar_assentos,
    salvar_assentos,
    init_sala,
    gerar_mapa
)

def vendInit():
    print("Olá, bem-vindo ao sistema de gerenciamento de tickets.")
    print("Você está logado como Vendedor.\n")

    salas_list = carregar_salas()
    salas = {s['numero']: s for s in salas_list}

    salas_list = carregar_salas()
    salas = {s['numero']: s for s in salas_list}
    assentos = carregar_assentos()

    while True:
        # 1) filmes
        print("\nFilmes disponíveis:")
        for i,f in enumerate(lista_filmes,1):
            print(f"  {i} - {f['titulo']}")
        esc = input("Escolha o número do filme: ").strip()
        if not esc.isdigit(): continue
        filme = lista_filmes[int(esc)-1]
        titulo = filme['titulo']
        # 2) salas do filme
        salas_filme = filme.get('salas', [])
        if not salas_filme:
            print(f"❌ '{titulo}' não está em nenhuma sala.")
            continue
        print(f"\nSalas com '{titulo}':")
        for i, sn in enumerate(salas_filme,1):
            s = salas[sn]
            print(f"  {i} - Sala {sn} ({s['linhas']}×{s['colunas']})")
        esc_s = input("Escolha a sala: ").strip()
        if not esc_s.isdigit(): continue
        sala_num = salas_filme[int(esc_s)-1]
        # inicializa assentos se necessário
        sala_info = salas[sala_num]
        init_sala(assentos, sala_num,
                  sala_info['linhas'],
                  sala_info['colunas'])
        # 3) exibe mapa
        print("\nMapa de assentos (XX = ocupado):")
        mapa = gerar_mapa(assentos[sala_num])
        for row in mapa:
            print("  " + " ".join(row))
        # 4) escolhe código
        escolha = input("Digite o código do assento: ").strip().upper()
        estado = assentos[sala_num].get(escolha)
        if estado is None:
            print("Código inválido.")
            continue
        if estado:
            print("Assento ocupado.")
            continue
        # 5) marca e salva
        assentos[sala_num][escolha] = True
        salvar_assentos(assentos)
        print(f"\n✅ Venda confirmada: '{titulo}', Sala {sala_num}, Assento {escolha}")

        if input("\nDeseja vender outro Ingresso? (s/n): ").lower() != "s":
            print("Encerrando vendas.")
            break

if __name__ == "__main__":
    vendInit()
