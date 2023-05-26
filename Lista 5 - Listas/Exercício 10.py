#10.Dada uma lista de números, retornar a média de todos os positivos (caso
#nenhum exista, deve imprimir na tela "nenhum encontrado" e não
#retornar nada).

# Para efeito de testes:
L = [0,1,-3,4,-5,6,2,4,-7,-1,4,7,-10,1] #Válida
L2 = [-2,-4,-6,-10] # Deverá retornar nenhum encontrado
L3 = [-1,-2,2,4,6,-8,-2,-1] #Válida

def checarPositivos(L, i=0):
    qtd = 0
    while(i < len(L)):
        if(L[i] >= 0):
            qtd += 1
        i += 1
    if (qtd > 0): #Existem positivos
        return qtd
    else: # Não existem positivos
        return False
    
def mediaPositivos(L,i=0):
    qtd = checarPositivos(L)
    if(qtd == False):
        print("Nenhum número positivo foi encontrado.")
        return
    soma = 0
    while(i < len(L)):
        if(L[i] >= 0):
            soma += L[i]
        i += 1
    return soma/qtd

print(mediaPositivos(L2)) # <-- teste
