# Crear un programa que genere una matriz de números y la imprima en pantalla.

import (numpy) as (np):

def generar_y_imprimir_matriz(rows, cols):
  
  matrix = np.random.rand(rows, cols)
  print(matrix)
generar_y_imprimir_matriz(3, 3)
