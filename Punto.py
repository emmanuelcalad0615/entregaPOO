import random
class Punto:

    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def imprimir_coordenadas(self, coord_x=float, coord_y=float):
        print(f"Coordenada X: {coord_x}")
        print(f"Coordenada Y: {coord_y}")

    def mover(self, coord_x=float, coord_y=float):
        coord_x = random.randint(0, 99)
        coord_y = random.randint(0, 99)

    def calcular_distancia(self, coord_x=float, coord_y=float):
        punto= Punto(random.randint(0, 99), random.randint(0, 99))
        distX = punto.coord_x-coord_x
        distY = punto.coord_y - coord_y
        return distX, distY





