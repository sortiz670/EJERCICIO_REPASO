# Crear una función que convierta grados Fahrenheit a grados Celsius

def fahrenheit_a_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9
  return celsius

print("Ingrese la temperatura en grados Fahrenheit ")
fahrenheit = float(input())
celsius = fahrenheit_a_celsius(fahrenheit)
print("La temperatura en grados Celsius es: ",celsius)