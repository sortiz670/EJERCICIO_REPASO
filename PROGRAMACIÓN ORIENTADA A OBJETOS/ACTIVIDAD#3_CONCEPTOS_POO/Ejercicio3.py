# A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

class Punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __str__(self):
      return f"({self.x}, {self.y})"
punto1 = Punto(3, 4)
print("Coordenadas del punto:",punto1)

def mover(self, nuevo_x, nuevo_y):
   self.x = nuevo_x
   self.y = nuevo_y
def calcular_distancia(self, otro_punto):
   distancia = match.sqrt((otro_punto.x - self.x))**2 + ((otro_punto.y - self.y)**2)
punto1 = Punto(3, 4)
punto2 = Punto(5, 6)

punto1.mostrar()
punto1.mover(5, 6)
punto1.mostrar()

distancia = punto1.calcular_distancia(punto2)
print("Distancia entre punto1 y punto2:",distancia)