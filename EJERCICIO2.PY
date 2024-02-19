# Escribir una función que calcule el área de un círculo dado su radio

import math


print("Ingrese el radio del circulo ")
radio = float(input())
area = math.pi * (radio * radio)
print("El area del circulo con radio ",radio,"Es: ",area)