#ejemplo 1
rta = "salida = | "
for numero in [1,2,3,4,5,6,7,8,9,10]: #Esto es una LISTA
 rta = rta + str (numero) + " , "
rta = rta + " | "
print(rta)

#Ejemplo 2
for numero in [1,2,3,4,5,6,7,8,9]:
 print("UIS NO ES UNO ")

#Ejemplo 3
rta = "salida = | "
for numero in (1,2,3,4,5,6,7,8,9,10): #Eso parentesis son una tumbla
 rta = rta + str (numero) + " , "
rta = rta + " | "
print(rta)

#Ejemplo
rta = "salida = | "
for numero in range(1,11):
 rta = rta + str (numero) + " , "
rta = rta + " | "
print(rta)

#Ejemplo 5
rta = "salida = | "
for numero in "UIS NO ES UNO":
 rta = rta + str (numero) + " , "
rta = rta + " | "
print(rta)

#Ejemplo 6
Suma = 0
for i in range(1,11):
 Suma = Suma + i
rta = rta + " | "
print(f"LA SUMA ES = {Suma}")



#Ejemplo 7
frase = input("digite una frase: ")
vocales = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
 if i in vocales:
  numero_vocales = numero_vocales + 1
print(f"En la frase hay {numero_vocales} vocales")

