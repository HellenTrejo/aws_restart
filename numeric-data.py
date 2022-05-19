print("Python has three numeric types: int, float, and complex")
 
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " es un tipo de dato " + str(type(myValue)))

myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " es un tipo de dato " + str(type(myValue)))

myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " es un tipo de dato " + str(type(myValue)))

myValue=True
print(myValue)
print(type(myValue))
print(str(myValue)+ " es un tipo de dato" + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue)+ " es un tipo de dato" + str(type(myValue)))

#Escribe un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

hora=float(input("Horas trabajadas: "))
coste=float(input("Coste por hora: "))
paga= hora * coste
print(paga)


#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla 
#la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso=int(input("Indique su peso: "))
altura=float(input("Indique su estatura: "))
imc= peso / (altura * altura)   
redondearImc = round(imc,2)
print(" Tu índice de masa corporal es " + str(redondearImc))


#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
#así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
#Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas 
#vendidos en el último pedido y calcule el peso total del paquete que será enviado.

muneco=int(input("Muñecos vendidos: "))
payaso=int(input("Payasos vendidos: "))
pesoMune=(muneco * 75) /1000
pesoPaya=(payaso * 112) /1000
pesoTotal= pesoMune + pesoPaya
print("El peso total es: " + str(round(pesoTotal, 2)) + " kg")