#5. Calcular a média de 2 números.

def CalcMedia2(n1,n2):
    return (n1+n2)/2

#7. Calcular a média de 4 números CHAMANDO A FUNÇÃO 5.

n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))

def CalcMedia4(n1,n2,n3,n4):
    media1 = CalcMedia2(n1,n2)
    media2 = CalcMedia2(n3,n4)
    return (media1+media2)/2

media4 = CalcMedia4(n1,n2,n3,n4)
print("A média entre os 4 números usando a função 5 é: ", media4)

    
