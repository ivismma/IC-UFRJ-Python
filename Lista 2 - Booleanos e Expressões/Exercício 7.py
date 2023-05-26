from math import *

def media(n1,n2):
    return (n1+n2)/2

def testaMedia(x,y,z):
    return (media(x,y) - 0.05 <= z <= media(x,y) + 0.05)

#Média entre 10 e 8 = 9
print(testaMedia(10,8,8.96)) #Tem que dar True
print(testaMedia(10,8,8.93)) #Tem que dar False