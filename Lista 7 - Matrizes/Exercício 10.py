#10.Dada uma matriz, retornar o menor elemento.
import random

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

def criaMatrizRandomizada(i,j):
    M = criaMatriz(i,j)
    for i in range(0, len(M)):
        for j in range(0,len(M[0])):
            M[i][j] = random.randint(10,100)
    return M

def menorValorMatriz(M):
    menor = M[0][0] 
    for i in range(0,len(M)):
        for j in range (1,len(M[0])): #Começa em M[0][1] pois o menor será o M[0][0] até que se encontre algum elemento menor do que ele (ou não).
            if(M[i][j] < menor): menor = M[i][j]
    return menor

M = criaMatrizRandomizada(3,3)
exibirMatriz(M)
print("")
print("O menor valor dessa matriz é:", menorValorMatriz(M))