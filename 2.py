#Una función que imprima el resultado de elevar un número a en b (es decir ab) sin utilizar  la  librería math . Hacer  esta  operación  dos  veces  y  comparar  el  primer resultado con el segundo, indicando cuál fue mayor.
#Primero nos toca recibir los dos valores a calcular
a=float(input("Bienvenido! Por favor ingresa el valor principal: "))
b=float(input("Ahora ingresa hacia lo que lo vas a elevar: "))
#Se crea la respuesta elevalda
x1=a**b
#Se imprime la respuesta
print("La respuesta de {} elevado a {} es: {}".format(a,b,x1))
#Se hace otra vez la operación mediante haciendolo a la inversa
x2=b**a