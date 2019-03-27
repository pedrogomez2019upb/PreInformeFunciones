#Una función que lea un número n imprima todos los números impares de 1 a n.
#Primero vamos a declarar los contadores necesarios para el desarrollo del ejercicio
n=0
i=0
#Se ingresa el número a contar
n=int(input("Bienvenido! Vamos a hacer un rango de valores para los números impares. Por favor ingresa el final del intervalo:"))
#Creamos un for para que empiece a hacer el ejercicio
for i in range (1,n):
    #Creamos la condicional necesaria para que siempre imprima los números impares
    if i%2 !=0:
        #Finalmente imprimimos el resultado
        print(i)
print("Muchas gracias por utilizar el programa.")
#Desarrollado por Pedro Gómez / ID:000396221
    
    
