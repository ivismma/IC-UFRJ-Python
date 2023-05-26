#Dada uma lista e um valor, retornar a lista com o valor inserido no
#início.

L = [0,1,2,5,6,7,9,11,23,87,11,10,15,67,3]
tamL = len(L)

n = int(input("Digite um valor: "))

def retornaLista(L,valor):
    L[1:15] = L[0:15]
    L[0] = n
    return L

print(retornaLista(L,n))