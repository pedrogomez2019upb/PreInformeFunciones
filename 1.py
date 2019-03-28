#Una función que lea un número n imprima todos los números impares de 1 a n.
#Definimos la función a utilizar
def impares(n):
        #Primero vamos a declarar los contadores necesarios para el desarrollo del ejercicio
        i=0
        #Creamos un for para que empiece a hacer el ejercicio
        for i in range (1,n):
                #Creamos la condicional necesaria para que siempre imprima los números impares
                if i%2 !=0:
                        #Finalmente imprimimos el resultado
                        print("El valor es: {}".format(i))
        print("Muchas gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221
    
impares(4)