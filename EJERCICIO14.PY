# Escribir una función que calcule la media aritmética de una lista de números.

def media_aritmetica(lista):
  suma = 0
  for numero in lista:
    suma += numero
  media = suma / len(lista)
  return media

lista = [1, 2, 3, 4, 5]
media = media_aritmetica(lista)
print("La media aritmética es:", media)
