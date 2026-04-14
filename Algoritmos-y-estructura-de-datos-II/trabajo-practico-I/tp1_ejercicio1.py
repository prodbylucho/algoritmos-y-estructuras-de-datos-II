class Vehiculo:
    def __init__(self, marca, velocidad_max):
        self.marca = marca
        self.velocidad_max = velocidad_max

    def describir(self):
        return f"Vehiculo de marca {self.marca}, con una velocidad maxima de {self.velocidad_max} km/h."

class Auto(Vehiculo):
    def __init__(self, marca, velocidad_max, puertas):
        super().__init__(marca, velocidad_max)
        self.puertas = puertas

    def describir(self):
        return f"Auto {self.marca}: Alcanza {self.velocidad_max} km/h y tiene {self.puertas} puertas."

class Moto(Vehiculo):
    def __init__(self, marca, velocidad_max, cilindrada):
        super().__init__(marca, velocidad_max)
        self.cilindrada = cilindrada

    def describir(self):
        return f"Moto {self.marca}: Alcanza {self.velocidad_max} km/h con una cilindrada de {self.cilindrada}cc."

mis_vehiculos = [
    Auto("Toyota", 180, 4),
    Moto("Honda", 120, 250),
    Auto("Ford", 200, 2)
]

print("--- Listado de Vehículos ---")
for v in mis_vehiculos:
    print(v.describir())
    