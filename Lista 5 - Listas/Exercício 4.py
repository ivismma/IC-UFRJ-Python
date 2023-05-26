#4. Retornar o índice da 1a ocorrência de um dado valor em uma dada lista.

L = [0,1,2,3,1,3,2,5,5,1,2,4,2,2,1,4,5,3,2,6,0,0,3,5,2,1]
tamL = len(L)

n = int(input("Digite o valor a ser procurado (0 a 6): "))

def retornaLista(L,n,i=0):
    while(i < tamL):
        if(L[i] == n):
            return i
        i += 1
    return False

print("O índice da 1ª ocorrência do valor dado é: ", retornaLista(L,n))