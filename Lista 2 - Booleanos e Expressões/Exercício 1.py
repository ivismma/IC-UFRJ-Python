#1. Dado um valor inteiro, retornar True se ele for par.

def retornaPar(num):
    if(num%2 == 0):
        return True
    else:
        return False

#Teste

n = int(input("Digite um número inteiro: "))
if(retornaPar(n) == True):
    print("O número inserido é par.")
else:
    print("O número inserido é ímpar.")

input("\nFim da execução.")