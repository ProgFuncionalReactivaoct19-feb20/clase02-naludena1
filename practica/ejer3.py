"""
	Practica: uso de funcion lambda
	@naludena1
"""

suma = ((10, 11))

dato1 = lambda x: x[0]
dato2 = lambda x: x[1]

result = (dato1(suma) + (dato2(suma)))
print(result)
