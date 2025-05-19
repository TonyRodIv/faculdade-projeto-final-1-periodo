import json
import os

ARQUIVO_SALAS  = os.path.join('data', 'temp', 'salas.json')
ARQUIVO_FILMES = os.path.join('data', 'temp', 'filmes.json')

def garantir_pasta(arquivo):
    pasta = os.path.dirname(arquivo)
    os.makedirs(pasta, exist_ok=True)

def carregar_json(arquivo):
    garantir_pasta(arquivo)
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_json(objetos, arquivo):
    garantir_pasta(arquivo)
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(objetos, f, ensure_ascii=False, indent=4)

salas  = carregar_json(ARQUIVO_SALAS)
filmes = carregar_json(ARQUIVO_FILMES)

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def listar_salas():
    if not salas:
        print("⚠️  Nenhuma sala cadastrada.")
        return
    print("Salas:")
    for s in salas:
        print(f" • Sala {s['numero']} - {s['cadeiras']} cadeiras")

def listar_filmes():
    if not filmes:
        print("⚠️  Sem filmes cadastrados.")
        return
    print("Filmes:")
    for f in filmes:
        print(f" • {f['titulo']} | {f['duracao']}min | {f['genero']} | Classif.: {f['classificacao']} | Sala: {f['sala']}")

def adicionar_filme():
    print("=== Adicionar Filme ===")
    titulo = input("Título: ").strip()
    chave = titulo.lower()

    if any(f['titulo'].lower() == chave for f in filmes):
        print(f"❌ Filme '{titulo}' já existe.")
        return

    duracao       = int(input("Duração (min): ").strip())
    classificacao = input("Classificação etária: ").strip()
    genero        = input("Gênero: ").strip()

    listar_salas()
    sala = input("Número da sala: ").strip()
    if not any(s['numero'] == sala for s in salas):
        print(f"❌ Sala {sala} não cadastrada.")
        return
    if any(f['sala'] == sala for f in filmes):
        print(f"❌ Sala {sala} já está ocupada por outro filme.")
        return

    filmes.append({
        "titulo":        titulo,
        "duracao":       duracao,
        "classificacao": classificacao,
        "genero":        genero,
        "sala":          sala
    })
    salvar_json(filmes, ARQUIVO_FILMES)
    print(f"✅ Filme '{titulo}' adicionado na sala {sala}.")

def remover_filme():
    print("=== Remover Filme ===")
    listar_filmes()
    if not filmes:
        return

    titulo = input("Título do filme a remover: ").strip()
    antes = len(filmes)
    filmes[:] = [f for f in filmes if f['titulo'].lower() != titulo.lower()]
    if len(filmes) < antes:
        salvar_json(filmes, ARQUIVO_FILMES)
        print(f"✅ Filme '{titulo}' removido.")
    else:
        print(f"❌ Filme '{titulo}' não encontrado.")

def editar_filme():
    print("=== Editar Filme ===")
    listar_filmes()
    if not filmes:
        return

    titulo = input("Título do filme a editar: ").strip()
    for f in filmes:
        if f['titulo'].lower() == titulo.lower():
            novo_titulo = input(f"Título (atual: {f['titulo']}): ").strip() or f['titulo']
            if novo_titulo.lower() != f['titulo'].lower() and \
               any(x['titulo'].lower() == novo_titulo.lower() for x in filmes):
                print(f"❌ Já existe filme com título '{novo_titulo}'.")
                return

            ndur = input(f"Duração (atual: {f['duracao']}): ").strip()
            ncla = input(f"Classif. (atual: {f['classificacao']}): ").strip()
            ngen = input(f"Gênero (atual: {f['genero']}): ").strip()

            listar_salas()
            nsal = input(f"Sala (atual: {f['sala']}): ").strip() or f['sala']
            if not any(s['numero'] == nsal for s in salas):
                print(f"❌ Sala {nsal} não existe.")
                return
            if nsal != f['sala'] and any(x['sala'] == nsal for x in filmes):
                print(f"❌ Sala {nsal} já ocupa outro filme.")
                return

            f['titulo']= novo_titulo
            if ndur: f['duracao']= int(ndur)
            if ncla: f['classificacao']= ncla
            if ngen: f['genero']= ngen
            f['sala']= nsal

            salvar_json(filmes, ARQUIVO_FILMES)
            print(f"✅ Filme '{novo_titulo}' atualizado.")
            return

    print(f"❌ Filme '{titulo}' não encontrado.")

def gerenciar_filmes():
    while True:
        clear_screen()
        print("=== Gerenciar Filmes ===")
        print("1. Adicionar")
        print("2. Remover")
        print("3. Listar")
        print("4. Editar")
        print("5. Voltar")
        opt = input("Opção (1–5): ").strip()

        if   opt == "1": adicionar_filme()
        elif opt == "2": remover_filme()
        elif opt == "3": listar_filmes()
        elif opt == "4": editar_filme()
        elif opt == "5":
            import adm
            adm.admInit()
        else: print("❌ Opção inválida.")

        input("\nEnter para continuar...")

# if __name__ == "__main__":
#     gerenciar_filmes()

