#7. Retorná-la com os mesmos elementos em ordem inversa.
#Ex.: [1, 3, 5, 7] [1, 3, 5, 7, 7, 5, 3, 1]

L = [1, 3, 5, 7]

def retornaLista(L):
    Laux = [] + L      #Cria a primeira metade
    for i in range(-1, -len(L)-1,-1):
        Laux.append(L[i])
    return Laux

print("Lista normal:", L)
print("Lista com o inverso:", retornaLista(L))