#8. Calcular a raiz quadrada de um número sem usar sqrt.

num = int(input("Digite um número para descobrir a raiz quadrada --> "))
def calcRaiz(num):
    return num**0.5

print("A raiz quadrada de", num, "é igual a:", calcRaiz(num))
