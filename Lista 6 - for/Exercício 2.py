# 2. Retorná-la com todos os elementos intercalados por zeros.
# Ex.: [1, 3, 5, 7] [1, 0, 3, 0, 5, 0, 7]
L = [1,3,5,7,9]

def retornaLista(L,i=0):
    tam = len(L)
    for i in range(0,  len(L) < (tam*2 - 1) , 2):
       L[i+1:i+1] = [0]
    return L

print("Lista normal:", L)
print("Lista intercalada:", retornaLista(L))
