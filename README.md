-Nombre: Lucio Aparicio
-Trabajo practico N°1
-Explicacion trabajo 1: Usamos la herencia definiendo la clase padre que seria vehiculo, que contiene las caracteristicas de marca y velocidad maxima, luego las clases hijas auto y moto heredan esas caracteristicas usando el super().__init__
luego cada clase hija agrega alguna caracteristica propia que la otra no tenga, el auto añade puertas y la moto cilindrada
luego uso el polimorfismo donde se llama a describir() y cada objeto responde con el formato que le corresponde.
-Explicacion trabajo 2: la clase padre usa herramientas que definen sus empleados (las clases hijas).
en la herencia el rectangulo y circulo ahorran codigo al heredar el atributo color de Figura
en la sobreescritura cada figura redefine el metodo area() con su formula matematica real (base por altura), ignorando el return 0 original
y en el polimorfismo interno: Lo mas ingenioso es el metodo describir(). aunque esta escrito en la clase padre, al ejecutar self.area(), python detecta automaticamente que figura es y aplica la formula correcta.
-Como correr el archivo: hacer clic en el icono de play en las esquina superior derecha del editor 
