#Dada uma lista e um valor, retornar a lista sem a 1a ocorrência do valor.

L = [0,1,2,2,3,4]
tamL = len(L)

n = int(input("Digite o valor a ser procurado (0 a 6): "))

def retornaLista(L,n,i=0):
    if(n == 0):
        return L[i+1:]
    else:
        while(i < tamL):
            if(L[i] == n & n != 0):
                return L[:i] + L[i+1:]
            i += 1
        return False #Não encontrou o valor

print(retornaLista(L,n))