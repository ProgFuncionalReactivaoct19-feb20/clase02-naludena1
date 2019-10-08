"""
	Practica: uso de funcion lambda
	@naludena1
"""

mensaje = ("Cuenca", "Azuay")

cadena_personalizada= lambda x, y: "%s capital de %s" %(x.upper(), y.upper())



print(cadena_personalizada("Cuenca", "Azuay"))