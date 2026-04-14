import math

class Figura:
    def __init__(self, color):
        self.color = color

    def area(self):
        return 0

    def describir(self):
        print(f"Soy una figura de color {self.color} y mi area es: {self.area():.2f}")

class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__(color)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

mis_figuras = [
    Rectangulo("Rojo", 10, 5),
    Circulo("Azul", 7),
    Rectangulo("Verde", 4, 4)
]

print("--- Resultados de las Figuras ---")
for i in mis_figuras:
    i.describir()