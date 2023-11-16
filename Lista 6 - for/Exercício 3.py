#Ordenação (Lista 5 - Ex 8)
L = [2,5,8,3,8,2,3,4,1,7]

#Algoritmo de ordenação genérico improvisado por mim, Complexidade do algoritmo não levado em conta.
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

#3. Seja a lista ordenada e dado um valor, retornar a lista com o valor
#inserido na posição correta sem reordená-la.
#Ex.: [1, 3, 5, 7, 9] e 6 [1, 3, 5, 6, 7, 9]

def inserirvalorLista(L, n, i=0):
    L = ordenarLista(L)
    for i in range(0, len(L)-1):
        if(L[i] <= n <= L[i+1]):
            L = L[:i+1] + [n] + L[i+1:]
            return L
    L.append(n)
    return L

#DEMONSTRAÇÃO:
print("Lista ordenada:", ordenarLista(L))

n = int(input("Digite o valor n: "))
print("Lista com valor inserido ordenado (sem reordenar):", inserirvalorLista(L, n))
