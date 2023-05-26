#1. Dada uma lista, retorná-la sem seu último elemento.

L = [0,1,2,5,6,7,9,11,23,87,11,10,15,67,3]
tamL = len(L)

def retornaLista(L):
    return L[0:14]

print(retornaLista(L))