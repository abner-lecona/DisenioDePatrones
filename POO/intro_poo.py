class Animal:
    def __init__(self, nombre, peso, sexo, edad, color):
        self.nombre = nombre
        self.peso = peso
        self.sexo = sexo
        self.edad = edad
        self.color = color

    def hacer_ruido(self):
        print(f"El animal {self.nombre} esta haciendo un ruido")

    def get_nombre(self):
        return self.nombre

class Gato(Animal):
    def __init__(self, nombre, peso, sexo, edad, color, es_sucio):
        super().__init__(nombre, peso, sexo, edad, color)
        self.es_sucio = es_sucio
    
    def hace_ruido(self):
        print(f"{self.nombre} hace miauuu")

class Perro(Animal):
    def __init__(self, nombre, peso, sexo, edad, color, mejor_amigo):
        super().__init__(nombre, peso, sexo, edad, color)
        self.mejor_amigo = mejor_amigo
    
    def hace_ruido(self):
        print(f"{self.nombre} hace guau")

a = Animal("Animal", "Peso", "Sexo", "Edad", "Color")
# print(a.get_nombre())

g = Gato("Zoro", 6, "M", 3, "Negro", True)
# print(g.get_nombre())
g.hace_ruido()

p = Perro("Eladio", 4, "M", 3, "Negro", "Andres")
p.hace_ruido()
