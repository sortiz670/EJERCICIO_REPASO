# Crear un programa que calcule la suma de los números en una lista dada

def suma_de_la_lista(lista_1):
    suma = 0
    for numero in lista_1:
        suma = suma + numero
    return suma

lista_1 = [1, 8, 20, 100, 50, 84]
print("La suma de la lista es:", suma_de_la_lista(lista_1))
