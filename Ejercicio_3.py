print("-------------------------------------")
print("-------------------------------------")
print("--------------DADOS------------------")
print("-------------------------------------")
print("-------------------------------------")

import random

n = int(input("NUMERO DE VECES QUE VA A LANZAR EL DADO: "))
resultado = 0
#contadores tipo string

cara1 = ""
cara2 = ""
cara3 = ""
cara4 = ""
cara5 = ""
cara6 = ""

for i in range (n):
    resultado = random.randrange(1,7)
    if resultado == 1:
        cara1 += "*"
    elif resultado == 2:
        cara2 += "*"
    elif resultado == 3:
        cara3 += "*"
    elif resultado == 4:
        cara4 += "*"
    elif resultado == 5:
        cara5 += "*"
    else:
        resultado == 6
        cara6 += "*"


print("Lado 1 " + str(cara1) )#colocar print de las veces
print("Lado 2 "+ str(cara2) )
print("Lado 3 "+ str(cara3))
print("Lado 4 "+ str(cara4))
print("Lado 5 "+ str(cara5))
print("Lado 6 "+ str(cara6))