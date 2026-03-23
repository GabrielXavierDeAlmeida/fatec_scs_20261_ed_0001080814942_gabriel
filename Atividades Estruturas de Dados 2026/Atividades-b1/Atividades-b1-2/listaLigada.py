'''
*---------------------------------------------------------*
* Fatec São Caetano do Sul *
* Exemplo de Manipulação de Lista ligada *
* Autor: Gabriel Xavier de Almeida *
* Objetivo:Mostrar manipulação de lista ligada em python *
* data: 15/03/2026 *
*---------------------------------------------------------*
'''
# Banco de dados em memoria (Dicionario)
produtos = {}

def valorExite(listaCabeca, valorEntrada):
    atual = listaCabeca
    while atual is not None:
        if atual ["valor"] == valorEntrada:
            return True
        atual = atual ["proximo"]
    return False

# funcao de InclusaoInicio
def inserirInicio(listaEntrada):
    valor = input("Digite o valor: ")
    if (valorExite(listaEntrada, valor)):
        print("Codigo de produto Duplicado")
        return listaEntrada
    novoNo = {"valor": valor, "proximo": listaEntrada}
    print("Produto Inserido")
    return novoNo

# 2 - Inserir no fim
def inserirFim(listaRecebida):
    valor = input("Digite o valor: ")
    if (valorExite(listaRecebida, valor)):
        print("Codigo de produto Duplicado")
        return listaRecebida
    novoNo = {"valor": valor, "proximo": None}
    listaAtual = listaRecebida
    if listaAtual is not None:
        while listaAtual["proximo"] is not None:
            listaAtual = listaAtual["proximo"]
        listaAtual["proximo"] = novoNo
        print("Produto Inserido")
        return listaRecebida
    else:
        return novoNo


# 3 - Inserir no meio
def inserirMeio(listaRecebida):
    valor = input("Digite o valor: ")
    if (valorExite(listaRecebida, valor)):
        print("Codigo de produto Duplicado")
        return listaRecebida
    posicaoInserir = int(input("Digite a posição que deseja inserir(o primeiro da lista é o 0): "))
    posicaoAtual = 0
    listaAtual = listaRecebida
    novoNo = {"valor": valor,"proximo": None}

    while listaAtual is not None:
        if posicaoAtual == posicaoInserir - 1:
            novoNo["proximo"] = listaAtual["proximo"] 
            listaAtual["proximo"] = novoNo
            print("Produto Inserido")
            return listaRecebida
        listaAtual = listaAtual["proximo"]
        posicaoAtual +=1
    print("Posição inexistente")
    return listaRecebida
            

# 4 - Listar
def listar(listaRecebida):
    if listaRecebida is None:
        print("Lista vazia")
        return
    listaAtual = listaRecebida
    while listaAtual is not None:
        print (listaAtual["valor"], end="->" )
        listaAtual = listaAtual["proximo"]

# 6 - Buscar Nó
def buscar(listaRecebida):
    argumentoPesquisa = input("Informe o argumento de pesquisa:")
    listaAtual = listaRecebida  
    posicao = 0
    encontrou = False

    while listaAtual is not None:
        if listaAtual["valor"]==argumentoPesquisa:
            encontrou = True
            break
        listaAtual = listaAtual["proximo"]
        posicao +=1
    if encontrou == False:
        print("Valor não encontrado")
    else:
        print(f"Valor encontrado na posição {posicao}")

# 5 - Remover Nó 
def remover(listaRecebida):
    valorRemover = input("Digite o valor que deseja remover: ")

    if listaRecebida is None:
        print("Lista vazia")
        return listaRecebida

    if listaRecebida["valor"] == valorRemover:
        return listaRecebida["proximo"]
    
    listaAnterior = listaRecebida
    listaAtual = listaRecebida["proximo"]  

    while listaAtual is not None:
        if listaAtual["valor"]==valorRemover:
            listaAnterior["proximo"] = listaAtual["proximo"]
            print("Produto removido")
            return listaRecebida
        listaAnterior = listaAtual
        listaAtual = listaAtual["proximo"]

    print("Valor não encontrado")
    return listaRecebida

    
# Exemplo de Menu de Interacao
def menu():
    lista = None
    while True:
        print("\n 1- Inserir no Início \n 2- Inserir no Fim \n 3- Inserir no Meio \n 4- Listar \n 5- Remover \n 6- Buscar \n 0- Sair")
        opcao = input("Escolha uma operação: ")

        if opcao == '1':
            lista = inserirInicio(lista)
        elif opcao == '2':
            lista = inserirFim(lista)
        elif opcao == '3':
            lista = inserirMeio(lista)
        elif opcao == '4':
            listar(lista)
        elif opcao == '5':
            lista = remover(lista)
        elif opcao == '6':
            buscar(lista)
        elif opcao == '0':
            print ("Obrigado por usar o sistema")
            break
        else:
            print ("**Opcao invalida**")

print ("**bemvindo ao programa**")
menu()