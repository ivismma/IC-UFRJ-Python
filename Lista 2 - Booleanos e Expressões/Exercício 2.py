#2. Fazer o mesmo para ímpar, chamando a função 1.

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