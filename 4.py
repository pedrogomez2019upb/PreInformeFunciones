#Realizar una función que permita saber si un número es o no “primo hermano”(Un número que preceda un primo y que no sea divisible entre 6)
#Primero hay que definir a funcion
def hermano():
    #Solicitamos el valor
    a=int(input("Hola! Vamos a ver si tu numero es primo hermano . Por favor ingresa el número: "))
    #Creamos los contadores
    contar=0
    contarP=0
    #Creamos la condicion if y then para saber si es divisibe por 6
    if (a%6==0) or (a==6):
        print("Lo siento , el número no es válido. Gracias por utilizar el programa.")
    else:
        #Usamos un while para que cuente los impares/pares
        while contar<=a+1:
            contar = contar + 1
            #Creamos otro if y then
            if (a+1) % contar ==0:
                contarP= contarP + 1
    #Creamos un if y then para saber si el contador tiene mas de dos divisores
        if contarP>=2:
            print("Lo siento, el número no es primo hermano. Gracias por utilizar el programa.")
        else:
            print("Que bien! Tu número es primo hermano. Gracias por utilizar el programa") 
#Desarrollado por Pedro Gómez / ID:000396221