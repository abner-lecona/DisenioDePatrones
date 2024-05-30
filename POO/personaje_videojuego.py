class Personaje:
    def __init__(self, nombre, vida_actual, ataque):
        self.nombre = nombre
        self.vida_actual = vida_actual
        self.ataque = ataque
    
    def visualiza_status(self):
        print(f" {self.nombre}")
        print(f" {self.vida_actual}")
        print(f" {self.ataque}")

    def esta_vivo(self):
        if self.vida_actual > 0:
            return True
        else: 
            return False
        
    def recibe_danio(self, cantidad):
        self.vida_actual -= cantidad
        if not self.esta_vivo():
            print(f"{self.nombre} se petateo X_X")
        else:
            print(f"Ahora {self.nombre} tiene {self.vida_actual} puntos de vida restantes")

    def ataca(self, enemigo):
        print(f"El personaje {self.nombre} esta atacando a {enemigo.nombre}")
        if enemigo.esta_vivo():
            enemigo.recibe_danio(self.ataque)

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida_actual=100, ataque=1000) # Aqui se hace la herencia
        self.cantidad_flechas = 20

    def visualiza_status(self):
        super().visualiza_status()
        print(f"{self.cantidad_flechas}")

    def ataca(self, enemigo):
        super().ataca(enemigo)
        self.cantidad_flechas -= 1

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida_actual=150, ataque=15)
        self.mana = 200

        def ataca(self, enemigo):
            print(f"El personaje {self.nombre} esta atacando a {enemigo.nombre}")
            if self.mana >20 and enemigo.esta_vivo():
                print(f"{self.nombre} lanza un hechizo contra {enemigo.nombre}")
                enemigo.recibe_danio(self.ataque)
                self.mana -= 20
            else: 
                print(f"Ya no hay mana")

class AsaltaCombis(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida_actual=100, ataque=50)


def combate(personaje1, personaje2):
    personaje1.ataca(personaje2)
    personaje2.visualiza_status()
    if personaje2.esta_vivo():
        personaje2.ataca(personaje1)
        personaje1.visualiza_status()

p2 = Personaje("Nombre2", 10, 10)
a1 = Arquero("Legolas")
m1 = Mago("Maguito")

combate(a1,m1)