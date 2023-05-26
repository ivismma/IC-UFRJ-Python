#1. Retornar o maior entre 3 valores dados (sem usar max)

def maiorNum(n1,n2,n3):
    if(n1 > n2 & n1 > n3):
        return n1
    else:
        if(n2 > n1 & n2 > n3):
            return n2
        else:
            return n3
        
n1 = int(input("Digite o 1º número inteiro: "))
n2 = int(input("Digite o 2º número inteiro: "))
n3 = int(input("Digite o 3º número inteiro: "))

print("O maior número é o:", maiorNum(n1,n2,n3))