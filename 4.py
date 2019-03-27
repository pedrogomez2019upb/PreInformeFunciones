#Realizar una función que permita saber si un número es o no “primo hermano”(Un número que preceda un primo y que no sea divisible entre 6)
#Primero hay que recibir el número a analizar
numero=int(input("Hola! Vamos a ver si el número ingresado es primo hermano. Por favor ingrese el número a analizar: "))
#Se crea un for para números primos y su contador que empice desde cero
contador = 0
for i in range(1,numero+1):
    if (numero% i)==0:
        contador = contador + 1
if contador==2:
    print ("El número ingresado es primo.")
    #Se añade la condicional para saber si es primo hermano mediante si es divisible por 6
    if numero/6 !=0 :
        print("El número ingresado es primo hermano. Gracias por utilizar el programa")
else:
    print ("El número ingesado no es primo y por ende no es primo hermano. Gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221