#Escribir una función que calcule el factorial de un número dado

def factorial(n):


  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

print("Ingrese un número: ")
n = int(input())
print("El factorial de", n, "es", factorial(n))
