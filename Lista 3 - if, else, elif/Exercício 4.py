#4. Retornar a média final de Computação I, dadas as notas das 2 provas
#(considere que faltar em uma prova recebe "nota" -1).

def mediafComp1(m1,m2):
    if(m1 == False): 
        m1 = -1
    if(m2 == False):
        m2 = -1
    return (m1+m2) / 2

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

print("Média Final:",mediafComp1(n1,n2))