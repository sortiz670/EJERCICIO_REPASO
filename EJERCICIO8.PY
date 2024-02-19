# Crear una función que invierta el orden de los elementos en una lista dada.

def invertir_lista(lista_1):
    lista_1.reverse()
    return lista_1

lista_1 = [1, 8, 20, 100, 50, 84]
print("Lista original:", lista_1)
lista_1 = invertir_lista(lista_1)
print("Lista invertida:", lista_1)
