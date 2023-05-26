
def fatorialRecursivo(num):
    if(num == 0):
        return 1
    else:
        return num*fatorialRecursivo(num-1)

def main():
    n = int(input("Fatorial (recursivo) de um número, digite um número --> "))
    res = fatorialRecursivo(n)
    print(n,"! = ", res, sep="")
    
    return 0

main()
