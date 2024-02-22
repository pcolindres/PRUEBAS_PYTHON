#Programación Orientada a Objetos (POO)

#1) Diseña una clase Vehiculo que demuestre los conceptos de POO como encapsulación, herencia y polimorfismo.
#2) Incluye validaciones en los métodos para manejar entradas incorrectas o situaciones inesperadas.
#3) Crea varias instancias de la clase y prueba sus métodos.
#4) Maneja errores y proporciona retroalimentación clara.

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def acelerar(self):
        raise NotImplementedError("El método 'acelerar' debe ser implementado en una subclase.")

    def frenar(self):
        raise NotImplementedError("El método 'frenar' debe ser implementado en una subclase.")

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, color):
        super().__init__(marca, modelo, año)
        self.color = color

    def acelerar(self):
        print(f"{self.marca} {self.modelo} ({self.año}) está acelerando.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} ({self.año}) está frenando.")


class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, año, traccion):
        super().__init__(marca, modelo, año)
        self.traccion = traccion

    def acelerar(self):
        print(f"{self.marca} {self.modelo} ({self.año}) con tracción {self.traccion} está acelerando.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} ({self.año}) con tracción {self.traccion} está frenando.")


# Prueba de la clase Coche
try:
    coche1 = Coche("Toyota", "Corolla", 2022, "rojo")
    print(coche1)
    coche1.acelerar()
    coche1.frenar()
except NotImplementedError as e:
    print(f"Error: {e}")

# Prueba de la clase Camioneta
try:
    camioneta1 = Camioneta("Ford", "Ranger", 2020, "4x4")
    print(camioneta1)
    camioneta1.acelerar()
    camioneta1.frenar()
except NotImplementedError as e:
    print(f"Error: {e}")

# Intentando crear un objeto Vehiculo (lo que debería fallar)
try:
    vehiculo_generico = Vehiculo("N/A", "Genérico", 2000)
    print(vehiculo_generico)
except NotImplementedError as e:
    print(f"Error: {e}")