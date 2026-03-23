"""
*********************************************************
*               Fatec Sâo Caetano do Sul
*                   Atividade B1-1
*           Autor: Gabriel Xavier de Almeida
*                   RA: 1681432612011
*  Objetivo: Aprender a manipular dicionários em python
*                   Data: 24-02-26
*********************************************************
"""
# Estrutura Global: Dicionário de Dicionários

catalogo = {}

def adicionar_filme(id_filme, titulo, diretor):
    """Insere um novo filme se o ID não existir."""
    if id_filme not in catalogo:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}
        print(f"filme adicionado {id_filme}, {titulo}, {diretor}")
    else:
        print("Esse id já existe")


def buscar_filme(id_filme):
    """Consulta um filme usando o método seguro .get()."""
    busca = catalogo.get(id_filme)
    if busca:
        print(f"filme encontrado id: {id_filme} ,titulo: {busca['titulo']} ,diretor: {busca['diretor']}")
    else:
        print("Esse id não existe")


def remover_filme(id_filme):
    """Remove um filme do dicionário usando .pop()."""
    if id_filme in catalogo:
        catalogo.pop(id_filme)
        print(f"filme removido com o id {id_filme}")
    else:
        print("Esse id não existe")


def listar_todos():
    """Itera sobre os itens do dicionário para listagem."""
    if not catalogo:
        print("\nO catalogo esta vazio.")
    else:
        print("\n--- Listagem de Filmes ---")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")


# --- Testes de Funcionamento ---
opcao = int(input("Escolha uma opção \n 1 - Adicionar filme \n 2 - Buscar filme \n 3 - Remover filme \n 4 - Listar todos os filmes \n 5 - Sair\n"))
while opcao != 5:
    if opcao == 1:
        id_filme = input("id do filme ")
        titulo = input("titulo do filme ")
        diretor = input("diretor do filme ")
        adicionar_filme(id_filme, titulo, diretor)
    elif opcao == 2:
        id_filme = input("id do filme ")
        buscar_filme(id_filme)
    elif opcao == 3:
        id_filme = input("id do filme ")
        remover_filme(id_filme)
    elif opcao == 4:
        listar_todos()
    else:
        print("Opção inválida, escolha entre 1 e 5")
    opcao = int(input("\nEscolha uma opção \n 1 - Adicionar filme \n 2 - Buscar filme \n 3 - Remover filme \n 4 - Listar todos os filmes \n 5 - Sair\n"))