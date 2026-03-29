"""----------------------------------------------------------------------------------
                                FATEC-São Caetano do Sul                 
                                    Estrutura de Dados                    
                                Id da Atividade: ED-Atividade-B1-3                            
    Objetivo: Desenvolver uma aplicação que simule o funcionamento lógico da calculadora
        financeira HP12c, utilizando os conceitos de Estrutura de Dados de Pilha (Stack)
        para o processamento de expressões em Notação Polonesa Reversa (RPN).               
                                Autor: Gabriel Xavier de Almeida              
                                    Data:29/03/2026
---------------------------------------------------------------------------------- """
def push(pilha, valor):
    pilha.pop(0)
    pilha.append(valor)

def realizar_operacao(pilha, operador):
    x = pilha.pop()
    y = pilha.pop()
    
    if operador == "+":
        resultado = y + x 
    elif operador == "-":
        resultado = y - x
    elif operador == "*":
        resultado = y * x
    elif operador == "/":
        resultado = y / x
    else:
        return print("Caracter inválido")
    
    t = pilha[0]
    pilha.insert(0, t)
    pilha.append(resultado)

def imprimir_pilha(pilha):
    t = pilha[0]
    z = pilha[1]
    y = pilha[2]
    x = pilha[3]
    print(f"T: {t}")
    print(f"Z: {z}")
    print(f"Y: {y}")
    print(f"X: {x}")
    print("--------")

rpn = input("Digite a expressão RPN ")
pilha = [0,0,0,0]
pilha_alg = []
qtde_elementos = rpn.split()
for i in qtde_elementos:       
    try:
        valor = float(i)
        push(pilha, valor)
        pilha_alg.append(str(valor))
        imprimir_pilha(pilha)
    except ValueError:
        if len(pilha_alg) < 2:
            print("Erro: operador sem operandos suficientes")
            break
        realizar_operacao(pilha, i)
        a = pilha_alg.pop()
        b = pilha_alg.pop()
        c = "(" + b + " " + i + " " + a + ")"
        pilha_alg.append(c)
        imprimir_pilha(pilha)
    
if len(pilha_alg) > 1:
    print("Erro: expressão inválida, operadores insuficientes")
elif len(qtde_elementos) < 2:
    print("Erro: expressão inválida")
else:
    print(f"Expressão algébrica: {c}")
    print(f"O resultado da expresão algébrica é: {pilha[3]}")