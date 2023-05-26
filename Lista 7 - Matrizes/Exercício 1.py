#1. Dada uma matriz A e um número n, retornar a multiplicação escalar n · A.
#Multiplicação escalar é o resultado da matriz inicial com todo seu Aij termo multiplicado por um número n

#Ex:                1  4  6       3  12  18
#   n = 3     3 *   4  2  1   =   12  6   3  

M = [ [1,6,4],
      [4,7,1],
      [8,4,2] ]

def exibirMatriz(M):
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def MultEscalarMatriz(M,n):
    for i in range(0, len(M)):
        for j in range(0, len(M[0])):
            M[i][j] *= n
    return M

print("Matriz:")
exibirMatriz(M)

print("")
n = int(input("Digite o valor da multiplicação escalar da matriz: "))
print("")

print("Matriz multiplicada: ")
exibirMatriz(MultEscalarMatriz(M,n))