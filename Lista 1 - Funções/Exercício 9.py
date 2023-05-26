#9. Calcule a hipotenusa de um triângulo retângulo, dados os catetos.
from math import sqrt
# a²+b²=c²

a = int(input("Insira o valor do 1º cateto (cm): "))
print("a =", a,"centímetros")
b = int(input("Insira o valor do 2º cateto (cm): "))
print("b =", b,"centímetros")

def calcHipotenusa(a,b):
    cquadrado = (a**2 + b**2)
    c = sqrt(cquadrado)
    return c

hipo = calcHipotenusa(a,b)
print("\nA hipotenusa desse triângulo retângulo equivale a:", hipo,"cm")

#10.Calcular o perímetro de um triângulo retângulo, dados os catetos e
#chamando a função 9.

def calcPerimetro(a,b,hipo):
    return (a+b+hipo)
perimetro = calcPerimetro(a,b,hipo)
print("O perímetro do triângulo retângulo é de:", perimetro, "centímetros")

input("\n\nFim da execução")
