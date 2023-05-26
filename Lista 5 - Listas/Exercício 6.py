#6. Dada uma lista, retorná-la invertida.

L = [0,1,2,2,3,4]
tamL = len(L)

def inverteLista(L, i=tamL-1):
    Laux = []
    while(i > 0):
        Laux.append(L[i])
        i -= 1
    return Laux

print(inverteLista(L))