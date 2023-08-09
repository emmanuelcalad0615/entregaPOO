import random
class Punto:

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def imprimir_coordenadas(self):
        print(f"Coordenadas: {self.coord_x}, {self.coord_y}")
    def mover(self, mover_x, mover_y ):
        self.coord_x=mover_x
        self.coord_y=mover_y
        print(f"El punto se ha movido a: {mover_x}, {mover_y}")
    def calcular_distancia(self, x, y):
        distancia_x= abs(x-self.coord_x)
        distancia_y= abs(y-self.coord_y)
        print(f"El punto se ha corrido {distancia_x} unidades en X y {distancia_y} en Y")


punto1 = Punto(3,4)

nuevo_x = random.randint(0,10)
nuevo_y = random.randint(0, 10)

punto1.imprimir_coordenadas()
punto1.mover(nuevo_x, nuevo_y)
punto1.calcular_distancia(nuevo_x,nuevo_y)


