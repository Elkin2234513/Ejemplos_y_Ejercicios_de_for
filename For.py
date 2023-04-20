#caso 1

x = range (10)


for i in (x):
    print(i)



#caso 2

x = range (10)
rta = "rango = "
for i in x:
    rta = rta + " , " + str(i)
rta = rta + " | "
print(rta)

x = range (3,10,2) #El tres hace que empiece en tres y el 2 hace que la serie salga solo numeros impares 
rta = "rango = "
for i in x:
    rta = rta + " , " + str(i)
rta = rta + " | "
print(rta)


#ejemplo 1
for i in [1,2,3,4,5,6,7,8,9.10]:
 rta = rta + str (i) + " , "
rta = rta + " | "
print(rta)
