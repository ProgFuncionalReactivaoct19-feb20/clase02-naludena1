"""
	Practica: uso de funcion lambda
	@naludena1
"""
import math # raiz cuadrada

datos = [(10,2), (8,7), (5,4), (3,11), (10,11)]

miFuncion1 = lambda x: x[0]
miFuncion2 = lambda x: x[1]

funcion = lambda x: (math.sqrt(miFuncion1(x)), miFuncion2(x)**2)

print(list(map(funcion, datos)))

