#Ordenação (Lista 5 - Ex 8)

L = [9, 5, 3, 1, 7, 3]

def ordenarLista(L, i=0, j=0):
    Laux = [] + L
    Lfinal = []
    for i in range(0, len(Laux)):
        menor=Laux[0]
        for j in range(1, len(Laux)):
            if(Laux[j] < menor):
                menor = Laux[j]
        Lfinal.append(menor)
        Laux.remove(menor)
    return Lfinal

def ordenarDecLista(L,i=0,j=0):
    L = ordenarLista(L)
    Laux = []
    for i in range(-1,-len(L)-1,-1):
        Laux.append(L[i])
    return Laux

#5. Retorná-la com a 1o metade da ordenada crescentemente e a 2a metade,
#decrescentemente.
#Ex.: [9, 5, 3, 1, 7, 3] [3, 5, 9, 7, 3, 1]

def retornaLista(L,i=0):
    L1 = []
    L2 = []
    for i in range(0, int(len(L)/2)):
        L1.append(L[i])
    while(i < len(L)-1): #Continuação da divisão de listas para segunda parte
        i += 1
        L2.append(L[i])
    return ordenarLista(L1) + ordenarDecLista(L2)

print(retornaLista(L))