from Electrodomestico import Electrodomestico


class Television(Electrodomestico):
    def __init__(self, precioBase = 100, color = "blanco", consumoEnergetico = 'F', peso = 5, resolucion = 20, fourK = False):
        Electrodomestico.__init__(self, precioBase = precioBase , color = color, consumoEnergetico = consumoEnergetico , peso = peso)
        self.resolucion = resolucion;
        self.fourK = fourK;

    def get_resolucion(self):
        return self.resolucion

    def get_fourk(self):
        return self.fourK

    def precioFinal(self):
        Electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.precioBase = self.precioBase * 1.3
        if self.fourK == True:
            self.precioBase = self.precioBase + 50