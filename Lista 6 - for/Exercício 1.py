#1. dada uma lista: Retorná-la sem elementos repetidos.
#Ex.: [3, 7, 9, 5, 3, 1, 9, 3] [7, 5, 1, 9, 3]

L = [3, 7, 9, 5, 3, 1, 9, 3]
L2 = [7, 5, 1, 9, 3]
tamL = len(L)


def sobrar1(L,qtd,n,i=0): #Remove os elementos repetidos deixando somente um único na lista.
    while(i < qtd-1):
        L.remove(n)
        i += 1
    return L

def checarLista(L, i=0, j=1): #Verifica se a lista tem elementos repetidos (pra saber se já está finalizada)
    while(i < len(L)-1):          #Retorna False: Existem elementos repetidos.
        while(j < len(L)):      #Retorna True: Não existem elementos repetidos (ok).
            if(L[i] == L[j]):
                return False
            j += 1
        i += 1
        j = i + 1
    return True

def retornaLista(L,i=0): #Retorna a lista sem elementos repetidos.
    while(checarLista(L) == False): # Enquanto existem elementos repetidos, continua...
        qtd = L.count(L[i])
        if(qtd > 1):
            L = sobrar1(L,qtd,L[i])
        i += 1
    return L

print("Lista:", L)
print("Lista (sem elementos repetidos):", retornaLista(L))