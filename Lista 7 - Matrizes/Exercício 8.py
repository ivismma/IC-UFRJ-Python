#Dada uma matriz, use duas das funções anteriores para retornar True se ela
#for triangular inferior e False caso contrário.

M = [[8,0,0,0,0],
     [0,7,0,0,0],
     [1,3,7,0,0],
     [2,2,0,2,0],
     [0,5,3,7,1] ]

def exibirMatriz(M): #Exibe a Matriz no seu formato correto.
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def verificaDiagonal(M): #Verifica se há algum zero na diagonal.
    i = 0
    j = 0
    while (i < len(M) and j < len(M[0])): #Elemento sempre será diagonal quando i = j | Ex: [2][2],[3][3],[5][5]
        if(M[i][j] == 0):
            return False #Achou um zero na diagonal, retorna
        i += 1
        j +=1
    return True #Não achou nenhum zero na diagonal, retorna

def verificaMatriz_Inferior(M):
    if(verificaDiagonal(M) == False): return False
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            if(j > i and M[i][j] != 0):
                return False
    return True

exibirMatriz(M)
print(verificaMatriz_Inferior(M))