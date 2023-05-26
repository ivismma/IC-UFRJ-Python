#5. Dada uma matriz, retornar uma lista com as médias de cada coluna.

M = [  [5,5,2],
       [8,6,3],
       [5,8,8] ]

def exibirMatriz(M): #Exibe a Matriz no seu formato correto.
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def mediaColuna(M): #Mais comentado do que o normal para eu usar como exemplo pra alguém ao ensinar/ajudar em Matrizes.
    L = [] #Lista que irá conter a média das colunas.
    soma = 0 #Var. que vai salvar as somas de cada coluna para efeito de cálculo da média.
    qtd = len(M)
    for i in range(0, qtd): #Esse for seleciona a coluna
        for j in range(0, len(M[0])): #Esse soma a coluna da vez.
            soma += M[j][i]
        L.append(round(soma/qtd,2)) #round para evitar floats gigantes (1.3333333, etc.)
        soma = 0 # A cada passo, zera a soma da coluna para a próxima.
    return L     #em C tem como adicionar mais de um passo como parâmetro simultaneamente dentro do for, Ex: for(j=0; j < TAM; j++,soma = 0){}

print("Matriz: ")
exibirMatriz(M)
print("Lista da média das colunas:", mediaColuna(M))