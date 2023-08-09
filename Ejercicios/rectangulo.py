class Punto:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

class Rectángulo:
    def __init__(self, esquina_sup_izq, esquina_inf_der):
        self.esquina_sup_izq = esquina_sup_izq
        self.esquina_inf_der = esquina_inf_der

    def tamaño_rect(self):
        #Utilizaré abs para obtener el valor absoluto de la operación, porque necesito valores positivos
        base = abs(self.esquina_inf_der.coord_x - self.esquina_sup_izq.coord_x)
        altura = abs(self.esquina_sup_izq.coord_y - self.esquina_inf_der.coord_y)
        return base, altura
    def area_rect(self, base, altura):
        area= base*altura
        return area
    def perimetro_rect(self,base, altura):
        perimetro= (base*2)+(altura*2)
        return perimetro
    def tipo_figuta(self, base, altura):
        if(base==altura):
            print("La figura es un cuadrado")
        else:
            print("La figura es un rectángulo ")

esquina_sup_izq = Punto(1, 4)
esquina_inf_der = Punto(6, 9)

rectangulo1 = Rectángulo(esquina_sup_izq, esquina_inf_der)

base, altura = rectangulo1.tamaño_rect()

area=rectangulo1.area_rect(base,altura)


perimetro=rectangulo1.perimetro_rect(base,altura)


print(f"El triangulo es de {altura}X{base}")
print(f"El area es= {area}")
print(f"El perímetro= {perimetro}")
rectangulo1.tipo_figuta(base,altura)






