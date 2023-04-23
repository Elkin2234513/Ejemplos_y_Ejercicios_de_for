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

#Ejemplos 8 Ingrese una frase y que diga cuantas veces se repite la a
frase = input("digite una frase: ")
vocalA = "a,A"
vocalE = "e,E"
vocalI = "i,I"
vocalO = "o,O"
vocalU = "u.U"


numero_vocalA = 0
numero_vocalE = 0
numero_vocalI = 0
numero_vocalO = 0
numero_vocalU = 0

for i in frase:
 if i in vocalA:
  numero_vocalA = numero_vocalA + 1
 elif i in vocalE:
  numero_vocalE = numero_vocalE + 1
 elif i in vocalI:
  numero_vocalI = numero_vocalI + 1
 elif i in vocalO:
  numero_vocalO = numero_vocalO + 1
 elif i in vocalU:
  numero_vocalU = numero_vocalU + 1




print(f"En la frase hay {numero_vocalA} de A")
print(f"En la frase hay {numero_vocalE} de E")
print(f"En la frase hay {numero_vocalI} de I")
print(f"En la frase hay {numero_vocalO} de O")
print(f"En la frase hay {numero_vocalU} de U")