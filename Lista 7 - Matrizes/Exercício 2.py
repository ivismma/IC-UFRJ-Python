#2. Dadas duas matrizes, retornar a soma.

M = [ [5,2,8],
      [1,9,3],
      [9,8,1] ]

M2 = [ [5,6,1],
       [9,9,2],
       [7,1,2] ]

def exibirMatriz(M):
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def somaMatrizes(M1,M2,i=0,j=0):
    for i in range(0,len(M)):
        for j in range(0,len(M[0])):
            M1[i][j] += M2[i][j]
    return M1
print("Matriz 1: ")
exibirMatriz(M)
print("Matriz 2: ")
exibirMatriz(M2)
print("Matriz somada: ")
exibirMatriz(somaMatrizes(M,M2))