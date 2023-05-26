#9. Dada uma matriz, use duas das funções anteriores para retornar True se ela
#for diagonal (elementos da diagonal principal diferentes de zero e
#elementos acima e abaixo da diagonal principal são zero), False c.c..

M = [[8,0,0,0,0],
     [0,7,0,0,0],
     [0,0,7,0,0],
     [0,0,0,2,0],
     [0,0,0,0,1] ]

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
            return False #Achou um zero na diagonal, retorna False
        i += 1
        j +=1
    return True #Não achou nenhum zero na diagonal, retorna True

def verificaMatrizDiagonal(M):
    for i in range(0, len(M)):
        for j in range(0,len(M[0])):
            if(i == j): continue             #Não vai testar a diagonal e vai prosseguir a iteração
            if(M[i][j] != 0): return False   #Encontrou um 0 fora da diagonal, ou seja, a matriz não é diagonal (somente diagonal sem zeros).
    if (verificaDiagonal): return True #A matriz é diagonal.
    else: return False

exibirMatriz(M)
print("")
print(verificaMatrizDiagonal(M))