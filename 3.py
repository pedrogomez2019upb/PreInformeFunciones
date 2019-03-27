#Realizar una función que permita saber si un número es o no primo
#Primero hay que recibir el número a analizar
numero=int(input("Hola! Vamos a ver si el número ingresado es primo. Por favor ingrese el número a analizar: "))
#Se crea una función para números primos
def primo(numero):
#Se hace un bucle para declarar cuando es primo
    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
#Ponemos ahora las condicionales necesarias para saber si es primo
if numero==0:
    break
if primo(numero):
    print ("\nEl numero %s es primo" % numero)
else:
    print ("\nEl numero %s NO es primo" % numero)
