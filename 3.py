#Realizar una función que permita saber si un número es o no primo
#Declarar la función para que funcione a base del "número"
def primo(numero):
    #Se crea un for para números primos y su contador que empice desde cero
    contador = 0
    for i in range(1,numero+1):
        if (numero% i)==0:
            contador = contador + 1
    if contador==2:
        print ("El número ingresado es primo. Gracias por utilizar el programa.")
    else:
        print ("El número ingesado no es primo. Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221