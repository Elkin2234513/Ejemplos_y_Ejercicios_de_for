print("-------------------------------------")
print("-------------------------------------")
print("-------DIVICIBLES ENTRES 7 Y 9-------")
print("-------------------------------------")
print("-------------------------------------")

#coloco primero dos contadores uno para el 7 y otro pal 9

Divicible_por_7 = 0
Divicible_por_9 = 0

for i in range(1000,5001):
    if i % 7 == 0:
        Divicible_por_7 +=1
    if i % 9 == 0:
        Divicible_por_9 +=1
print("El numero de divicibles por 7 es "+ str(Divicible_por_7))
print("El numero de divicibles por 9 es "+ str(Divicible_por_9))