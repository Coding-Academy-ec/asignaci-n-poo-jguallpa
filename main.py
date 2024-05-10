import math

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        areas= self.base * self.altura  # implementación de la función con la formula de área de un rectángulo
        return areas

rectangulo = Rectangulo(5, 7)
print (f"Area del rectanguo e: {rectangulo.area()}")

class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.__radio= radio  # inicialización de la variable radio

    def area(self):
        areas = math.pi * self.__radio**2 # implementación de la función con la forula de área de un círculo
        return areas
    

cir = Circulo(5)
print(f"Area del circulo es: {cir.area()}")