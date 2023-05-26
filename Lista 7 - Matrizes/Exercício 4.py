#4. Dada uma matriz quadrada, retornar True se ela for simétrica (igual à
#transposta), False caso contrário.

M = [ [1,7,12],
      [4,-4,6],
      [9,0,5] ]

M2 = [ [5,1,2],
       [1,6,3],
       [2,3,8] ]

def exibirMatriz(M): #Exibe a Matriz no seu formato correto.
    for i in range(0, len(M)):
        for j in range(0, len (M[0])):
            print(M[i][j], end="   ")
        print()
    return

def criaMatriz(i,j): #Inicializa a matriz, os parâmetros iniciais são, respectivamente, linhas e colunas desejadas.
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

# Matriz quadrada é aquela que possui mesma quantidade de linhas e colunas.

def verificaM_Quadrada(M): 
    if(len(M) == len(M[0])): #len(M) = quantidade de linhas | len(M[0]) = quantidade de colunas
        return True # i = j   < -- > é matriz quadrada
    else:
        return False # não é matriz quadrada.

def verificaSimetria(M):
    if(verificaM_Quadrada(M)):
        M2 = retornaTransposta(M) # M2 é a matriz que faz a transposta da Matriz M, para efeito de teste, e depois...
        if(M == M2):        # <--  ela é comparada a M para verificar se nenhum valor mudou, ou seja, é simetrica.
            return True
        else: # Se houve alteração, então não é simétrica, retorna False.
            return False
    else: # Nesse caso a matriz nem sequer é quadrada, então não pode ser testada.
        print("A matriz não foi testada pois não é quadrada.")
        return
    
print(verificaSimetria(M))
print(verificaSimetria(M2))