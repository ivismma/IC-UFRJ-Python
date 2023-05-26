#6. Dadas duas matrizes, retornar a multiplicação da 1a pela 2a.

M1 = [ [1,7,4],
      [8,3,9],
      [2,5,4] ]

M2 = [ [2,9,5],
       [4,1,0],
       [3,7,5] ]

def exibirMatriz(M): #Exibe a Matriz no seu formato correto.
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def criaMatriz(i,j): #Inicializa a matriz com zeros, os parâmetros iniciais são, respectivamente, linhas e colunas desejadas.
    M = []
    for i in range(i):
        M.append([0]*j)
    return M

def multiplicaMatrizes(M1,M2):
    for i in range(0,len(M1)):
        for j in range(0,len(M1[0])):
            M1[i][j] *= M2[i][j]
    return M1

exibirMatriz(M1)
print("")
exibirMatriz(M2)
print("Resultado:")
exibirMatriz(multiplicaMatrizes(M1,M2))