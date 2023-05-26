#Dada uma lista e um valor, retornar a lista com o valor inserido no
#início.

L = [0,1,2,3,1,3,2,5,5,1,2,4,2,2,1,4,5,3,2,6,0,0,3,5,2,1]
tamL = len(L)

n = int(input("Digite o valor a ser procurado (0 a 6): "))

def retornaLista(L,n,i=0):
    qtd = 0
    while(i < tamL):
        if(L[i] == n):
            qtd += 1
        i += 1
    return qtd

print("O valor digitado possui", retornaLista(L,n), "aparições na lista.")
