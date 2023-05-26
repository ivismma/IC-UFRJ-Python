#3. Dada uma matriz, retornar a transposta.
#Matriz transposta é o resultado da Matriz Aij de origem resultando seu elementos invertidos, isto é: ij --> ji

# i = linhas
# j = colunas

M = [ [1,7,12],
      [4,-4,6],
      [9,0,5] ]

def exibirMatriz(M):
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def criaMatriz(i,j):
    M = []
    for i in range(i):
        M.append([0]*j)
    return M

def retornaTransposta(M):
    M_aux = criaMatriz(len(M[0]),len(M))

    for i in range(0, len(M)):
        for j in range (0, len(M[0])):
            M_aux[i][j] = M[j][i]
    return M_aux

exibirMatriz(M)
print()
exibirMatriz(retornaTransposta(M))