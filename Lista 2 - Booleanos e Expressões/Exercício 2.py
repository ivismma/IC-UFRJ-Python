#2. Fazer o mesmo para ímpar, chamando a função 1.

def retornaPar(num):
    return True if not (n%2) else False
#Teste

n = int(input("Digite um número inteiro: "))
if(retornaPar(n) == True):
    print("O número inserido é par.")
else:
    print("O número inserido é ímpar.")

input("\nFim da execução.")
