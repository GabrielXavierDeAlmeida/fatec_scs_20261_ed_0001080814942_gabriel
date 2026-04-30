"""
*********************************************************
*               Fatec Sâo Caetano do Sul
*                   Atividade B2-2
*           Autor: Gabriel Xavier de Almeida
*                   RA: 1681432612011
*      Objetivo: Aprender a manipular filas em python
*                   Data: 30-04-26
*********************************************************
"""

from collections import deque

fila_aluno = deque()
fila_adm = deque()
fila_total = deque()

def inserir_documento(tipo):
    nome = input("Digite o nome do solicitante: ")
    nome_arq = input("Digite o nome do arquivo: ")
    total_paginas = int(input("Digite o total de páginas: "))

    documento = {"nome": nome, "nomeArq": nome_arq, "totalPaginas": total_paginas}
    
    if tipo == "aluno":
        fila_aluno.append(documento)
        print("Documento adicionado à fila de Alunos.")
    else:
        fila_adm.append(documento)
        print("Documento adicionado à fila ADM.")

def consumir_fila():
    if fila_total:
        doc = fila_total.popleft()
        print(f"\n[IMPRIMINDO] Arquivo: {doc['nomeArq']} | Solicitante: {doc['nome']}")
    else:
        print("A lista está vazia")

def listar_filas():
    print("\n--- ESTADO ATUAL DAS FILAS ---")
    print(f"ADM: {len(fila_adm)} documento(s) em espera.")
    for doc in fila_adm:
        print(f"  > {doc['nomeArq']} ({doc['totalPaginas']} págs) - {doc['nome']}")
    
    print(f"ALUNOS: {len(fila_aluno)} documento(s) em espera.")
    for doc in fila_aluno:
        print(f"  > {doc['nomeArq']} ({doc['totalPaginas']} págs) - {doc['nome']}")

    print(f"TOTAL: {len(fila_total)} documento(s) em espera.")
    for doc in fila_total:
        print(f"  > {doc['nomeArq']} ({doc['totalPaginas']} págs) - {doc['nome']}")

    print("------------------------------")

def reorganizar_filas():
    if len(fila_total) > 0:
        print("ERRO: Não é possível reoganizar sem ela estar vazia")
        return

    while fila_adm:
        fila_total.append(fila_adm.popleft())
    
    while fila_aluno:
        fila_total.append(fila_aluno.popleft())
    print("Fila reorganizada com sucesso!")

print("** Sistema de Impressão Acadêmica **")
while True:
    print("\n1- Inserir Aluno \n2- Inserir ADM \n3- Consumir (Imprimir) \n4- Listar Filas \n5- Reorganizar \n0- Sair")
    opcao = input("Escolha uma operação: ")

    if opcao == '1':
        inserir_documento("aluno")
    elif opcao == '2':
        inserir_documento("adm")
    elif opcao == '3':
        consumir_fila()
    elif opcao == '4':
        listar_filas()
    elif opcao == '5':
        reorganizar_filas()
    elif opcao == '0':
        print("Encerrando sistema...")
        break
    else:
        print("** Opção inválida **")