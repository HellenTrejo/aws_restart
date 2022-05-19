"""
userRespuesta = input("Necesita enviar un paquete?(Ingrese si o no) ")

if(userRespuesta == "si"):
    print("Nosotros podemos ayudarte enviando ese paquete!")
else:
    print("Por favor, regrese cuando necesite enviar un paquete. Gracias")
"""

userReply = input("¿Le gustaría comprar estampas comprar un sobre o hacer una copia? (Ingrese estampas, sobre o copia) ")
if userReply == "estampas":
    print("Tenemos muchos diseños de estampas para elegir.")
elif userReply == "sobre":
    print("Tenemos muchos tamaños de sobres para elegir.")
elif userReply == "copia":
    copia=input("¿Cuántas copias quieres? (Ingrese un numero) ")
    print("Aquí están tus {} copias".format(copia))
else:
    print("Gracias, por favor venga de nuevo")