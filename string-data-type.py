myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " es un tipo de dato " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

"""
nombre = input("Cual es su nombre? ")
print(nombre)

color = input("Cual es su color favorito? ")
animal = input("Cual es su animal favorito? ")
print("{}, te gusta un {} {}!" .format(nombre,color,animal))
"""
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero 
#e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nombre = input("Ingrese su nombre ")
numero = int(input("Ingrese un numero "))
print(str(nombre+"\n") * numero)
"""

#Escribir un programa que pregunte el nombre completo del usuario en la consola 
#y después muestre por pantalla el nombre completo del usuario tres veces,
#una con todas las letras minúsculas, otra con todas las letras mayúsculas 
#y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""
nombreCompleto = input("Ingrese su nombre completo: ")
print(nombreCompleto.lower())
print(nombreCompleto.upper())
print(nombreCompleto.title())
"""


#Escribir un programa que pregunte el nombre del usuario en la consola y 
#después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
#tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas 
#y <n> es el número de letras que tienen el nombre.
nombre= input("Ingrese su nombre: ")
print( nombre.upper() + " tiene " + str(len(nombre)) + " letras")
