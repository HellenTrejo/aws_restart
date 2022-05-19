myFruitList= ["manzana", "platano", "cereza"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2]="orange"
print(myFruitList)

myFinalAnswerTuple = ("manzana", "platano", "piña")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


myFavoriteFruitDictionary = {
    "Akua" : "manzana",
    "Saavi" : "platano",
    "Paulo" : "piña"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saavi"])
print(myFavoriteFruitDictionary["Paulo"])


##Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
cursosList=["Física", "Química", "Historia", "Lengua"]
print(cursosList)
for item in cursosList:
    print(str(item))
    
#Escribir un programa que pida al usuario las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y
#solicitar la nota de cada asignatura en otra lista y luego muestre por pantalla el mensaje 
#Yo estudio la <asignatura> y he sacado <nota>

cursoList=[]
notaList=[]

cant=int(input("Cuantos cursos desea ingresar: "))
for item in range(cant):
    curso = input("Ingrese nombre del curso: ")
    nota = int(input("Ingrese la nota: "))
    cursoList.append(curso)
    notaList.append(nota)
    print("Yo estudio "+ curso + " y he sacado " + str(nota))
    item+=1
        
print(cursoList)
print(notaList)

    
"""
#Codigo del compañero
lista_asignaturas = []
lista_notas = []

x =  int(input("Ingrese el número de asiganturas a registrar: "))
for x in range(x):  
    lista_asignaturas.append(input("Ingrese la asignatura que cursó: "))
    lista_notas.append(input("Ingrese la nota que sacó en la asignatura: "))
    
for item in zip (lista_asignaturas, lista_notas):
     print("Yo estudié", item[0],"y he sacado", item[1])
"""
