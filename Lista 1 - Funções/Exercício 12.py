
#Ex 12.Calcular as raízes reais de uma equação do 2o grau dados seus
#parâmetros a, b e c.
from math import sqrt

a = int(input("Digite o valor a: "))
b = int(input("Digite o valor b: "))
c = int(input("Digite o valor c: "))

def criaString(a,b,c): #ax²+bx+c
    string = ""
    ## Criando 1ª parte da equação:
    if (a == 1 or a == -1):
        if( a < 0):
            st1 = "-"
        else:
            st1 = ""
    else:
        st1 = ""
    ## Criando 2ª parte da equação:
        if (b > 0):
            st2="x²+"
        else:
            st2="x²"
    ## Criando 3ª parte da equação:
        if (c > 0):
            st3="+"
        else:
            st3=""
    ## Formulando a equação na string:
        if( a == 1):
            string = st1 + st2 + str(b) + "x" + st3 + str(c)
        else:
            string = st1 + str(a) + st2 + str(b) + "x" + st3 + str(c)
    return string
3
criaString(a,b,c)
print("\n",criaString(a,b,c),"\n")
## Resolvendo a equação:

def descobreRaizes(a,b,c):
    delta = (b**2) - (4*a*c)
    if (delta < 0):  #Não existem raízes reais.
        print("Δ =", delta, "| Δ < 0, a equação não possui raízes reais.")
        return False 
    if (delta == 0): #Raíz única
        x1 = -b/(2*a)
        print("x1 =", x1)
    else:            #Duas raízes
        raizdelta = sqrt(delta)
        x1 = (-b +raizdelta)/(2*a)
        x2 = (-b -raizdelta)/(2*a)
        print("x1 =", x1)
        print("x2 =", x2)
    return True

descobreRaizes(a,b,c)

input("\n\nFim da execução.")