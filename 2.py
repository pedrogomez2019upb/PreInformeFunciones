#Una función que imprima el resultado de elevar un número a en b (es decir ab) sin utilizar  la  librería math . Hacer  esta  operación  dos  veces  y  comparar  el  primer resultado con el segundo, indicando cuál fue mayor.
#Se crea la función para que lea los valroes a b c y d
def elevar():
    #Primero nos toca recibir los dos valores a calcular
    a=float(input("Bienvenido! Por favor ingresa el valor principal: "))
    b=float(input("Ahora ingresa hacia lo que lo vas a elevar: "))
    #Se crea la respuesta elevalda
    x1=a**b
    #Se imprime la respuesta
    print("La respuesta de {} elevado a {} es: {}".format(a,b,x1))
    c=float(input("Bienvenido! Por favor ingresa el valor principal 2: "))
    d=float(input("Ahora ingresa hacia lo que lo vas a elevar 2: "))
    #Se hace otra vez la operación mediante haciendolo a la inversa
    x2=c**d
    #Se imprime el segundo resultado
    print("La inversa de la respuesta es: {}".format(x2))
    #Se pone las condicionales para saber cual es mayor que otro
    if x1>x2:
        print("La primera respuesta es mayor que la segunda. Gracias por utilizar el programa.")
    else:
        if x1==x2:
            print("Las dos respuestas son iguales. Gracias por utilizar el programa")
        else:
            print("La segunda respuesta es mayor a la primera. Gracias por utilizar el programa")
#Desarrollado por Pedro Gómez / ID:000396221