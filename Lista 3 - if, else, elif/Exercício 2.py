#2. Dados 3 valores, retorná-los em ordem crescente.

def ordernarCrescente(n1,n2,n3):
    if( (n1 > n2) & (n1 > n3) ): #n1 é o maior.
        if(n2 > n3): #n2 é o 2º e n3 3º.
            return n3,n2,n1
        else: #n3 é o 2º e n2 o 3º.
            return n2,n3,n1

    else:
        if( (n2 > n1) & (n2 > n3) ): #n2 é o maior.
            if(n1 > n3): #n1 é o 2º e n3 o 3º.
                return n3,n1,n2
            else: #n3 é o 2º e8 n1 o 3º.
                return n1,n3,n2
        else: #n3 é o maior.
            if( (n1 > n2) & (n1 > n3) ): #n1 é o 2º maior e n2 o 3º
                return n2,n1,n3
            else: #n2 é o 2º maior e n1 o 3º
                return n1,n2,n3

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

print(ordernarCrescente(n1,n2,n3))