class Vehiculo:
    def __init__(self, velociadad_maxima, kilometraje):
        self.velocidad_maxima = velociadad_maxima
        self.kilometraje = kilometraje

auto1=Vehiculo(200,300)

print(f"Velocidad Máxima: {auto1.velocidad_maxima}")
print(f"Kilometraje: {auto1.kilometraje}")
