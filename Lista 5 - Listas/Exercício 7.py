#7. Dada uma lista, retornar seu menor elemento (sem usar a função "min").

L = [0,1,2,3,5,4,1,2,32,3,4,5,6,8,2,4,11]
tamL = len(L)

def retornaMenor(L, i=1):
    menor = L[0]
    while (i < tamL):
        if(L[i] < menor):
            menor = L[i]
        i += 1
    return menor

print("O menor número da lista dada é:", retornaMenor(L))