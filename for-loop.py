print("Count to 10!")
for x in range (0, 11):
    print(x)
    
    
#Escribir un programa que pregunte al usuario una frase y una letra, 
#recorrer la frase  en busca de la letra e identificar el numero de vesces que aparece la letra en la frase y mostrarlo por pantalla

frase = input("Escriba una frase: ")
letra = input("Escriba una letra: ")
counter=0
for x in frase:
    if(x == letra):
        counter+=1
  
print("La letra {} se menciona: {} veces".format(letra,counter))

