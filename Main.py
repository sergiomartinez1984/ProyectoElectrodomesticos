from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Television import Television

electrodomestico = ()
electrodomesticos = list(electrodomestico)

electrodomesticos.insert(-1, Electrodomestico(consumoEnergetico="A", peso=15))
electrodomesticos.insert(-1, Electrodomestico(consumoEnergetico="A", peso=30))
electrodomesticos.insert(-1, Electrodomestico(consumoEnergetico="A", peso=60))
electrodomesticos.insert(-1, Electrodomestico(consumoEnergetico="A", peso=90))

electrodomesticos.insert(-1,Lavadora(consumoEnergetico="E", peso=50, carga=30))
electrodomesticos.insert(-1,Lavadora(consumoEnergetico="A", peso=50, carga=60))

electrodomesticos.insert(-1, Television(peso=20, resolucion=30))
electrodomesticos.insert(-1, Television(peso=20, resolucion=50))

television = 0
lavadora = 0
electro = 0
i = 0

for electrodomestico in electrodomesticos:
    i += 1
    electrodomestico.precioFinal()
    if isinstance(electrodomestico,Television):
        television += electrodomestico.precioBase
    elif isinstance(electrodomestico,Lavadora):
        lavadora += electrodomestico.precioBase
    else:
        electro=electrodomestico.precioBase

print("Total de televisores: " + repr(television))
print("Total de lavadoras: " + repr(lavadora))
print("Total de electrodomésticos: " + repr(electrodomestico))

print("Total: " + repr(television+lavadora+electro))