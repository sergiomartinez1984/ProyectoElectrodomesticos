class Electrodomestico:

    def __init__(self, precioBase= 100,color= "blanco",consumoEnergetico ='F',peso =5):

            self.precioBase = precioBase
            self.color = color
            self.comprobarConsumoEnergetico(consumoEnergetico)
            self.peso = peso

    def get_precioBase(self):
            return self.precioBase

    def get_color(self):
            return self.color

    def get_comprobarConsumoEnergetico(self):
            return self.comprobarConsumoEnergetico

    def get_peso(self):
            return self.peso


    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A", "B", "C", "D", "E", "F"):
            self.consumo = letra


    def comprobarColor(self,color):
        if color in ("blanco", "negro", "rojo", "azul", "gris"):
            self.color = color

    def precioFinal(self):
        if self.consumo == 'A':
            self.precioBase = self.precioBase + 100
        elif self.consumo == 'B':
            self.precioBase = self.precioBase + 80
        elif self.consumo == 'C':
            self.precioBase = self.precioBase + 60
        elif self.consumo == 'D':
            self.precioBase = self.precioBase + 50
        elif self.consumo == 'E':
            self.precioBase = self.precioBase + 30
        elif self.consumo == 'F':
            self.precioBase = self.precioBase + 10

        if 0 < self.peso < 20:
            self.precioBase = self.precioBase + 10
        elif 20 < self.peso < 49:
            self.precioBase = self.precioBase + 50
        elif 50 < self.peso < 79:
            self.precioBase = self.precioBase + 80
        elif self.peso < 80:
            self.precioBase = self.precioBase + 100

