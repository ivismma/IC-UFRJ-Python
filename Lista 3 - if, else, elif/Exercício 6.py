#6. Dado um número inteiro, imprimir na tela se ele é maior que 0, maior
#que 10 ou maior que 100 (apenas um desses). Use apenas um operador
#relacional em cada condição e sem comandos aninhados.

def checarNum(n):
    if(n > 0):
        print("O número inserido é maior que zero.")
        return
    if(n > 10):
        print("O número inserido é maior que 10.")
        return
    if(n > 100):
        print("O número inserido é maior que 100.")
        return
    