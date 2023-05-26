#8. Dada uma lista, retorná-la ordenada.

L = [2,3,5,4,1,2,32,3,4,5,6,8,2,4,11]
tamL = len(L)

def retornaMenor(L, i=1):
    if(L == []):
        return False
    menor = L[0]
    while (i < len(L)):
        if(L[i] < menor):
            menor = L[i]
        i += 1
    return menor

def apagaValor(L,n,i=0): #Apaga todos os valores --> n <-- da lista
    while(L.count(n)):
        L.remove(n)
    return L

def ordenarLista(L, i=0):
    Laux = []
    while(len(L)):
        ordem = retornaMenor(L) #Vai sequenciando do menor para o maior
        qtd = L.count(retornaMenor(L)) #Quantas ocorrências do número da vez pra adicionar.
        L = apagaValor(L,ordem) #Remove o valor inserido da lista até ela esvaziar
        while(i < qtd):
            Laux.append(ordem)
            i+=1
        i = 0
    return Laux

print(retornaMenor(L))
print("Lista normal:", L)
print("Lista ordenada:", ordenarLista(L))