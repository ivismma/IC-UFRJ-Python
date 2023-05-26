#Dada uma lista de inteiros, retorná-la com o sinal de todos os valores
#ímpares invertidos, imprimindo na tela quantos são.

L = [2,3,5,4,1,2,32,3,4,5,6,8,2,4,11]
tamL = len(L)

def inverteImpares(L, i=0):
    qtd = 0
    while(i < tamL):
        if(L[i]%2 != 0): # é ímpar
            L[i] = -L[i]
            qtd += 1
        i += 1
    print(L)
    print("Total de pares invertidos:", qtd)
    return

print("Lista:", L)
inverteImpares(L)