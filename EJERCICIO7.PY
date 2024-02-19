# Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

def encontrar_maximo_y_minimo(lista_1):
    maximo = lista_1[0]
    minimo = lista_1[0]
    for numero in lista_1:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    return maximo, minimo

lista_1 = [1, 8, 20, 100, 50, 84]
maximo, minimo = encontrar_maximo_y_minimo(lista_1)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)
