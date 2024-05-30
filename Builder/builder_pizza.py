# class Pizza:

# def __init__(size: int, cheese: bool, pepperoni: bool, 
# chile: bool, basil: bool, extra_sauce: bool, ham: bool, 
# extra_cheese: bool, pineapple: bool, mushroom: bool):
    
class Pizza:
    def __init__(self, especificaciones, tamanio, salsa, queso):
        self.tamanio = tamanio
        self.salsa = salsa
        self.queso = queso
        self.especificaciones =  especificaciones

    def show(self):
        print(f"Las caracteristicas de la pizza son: {self.tamanio,self.queso,self.salsa,self.especificaciones}")


class Builder:
    def __init__(self, tamanioo, salsaa, quesoo):
        self.reset()
        self.tamanioo = tamanioo
        self.salsaa = salsaa
        self.quesoo = quesoo

    def reset(self):
        self.especificaciones = []

    def tamanio(self, tamanioo):
        if tamanioo == "G":
            self.tamanioo = "Grande"
        elif tamanioo == "M":
            self.tamanioo = "Mediana"
        elif tamanioo == "C":
            self.tamanioo = "Chica"

    def queso(self, quesoo):
        if quesoo == "SQ":
            self.quesoo = "Sin queso"
        elif quesoo == "CQ":
            self.quesoo = "Con queso"
        elif quesoo == "EQ":
            self.quesoo = "Extra queso"
    
    def salsa(self, salsaa):
        if salsaa == "SS":
            self.salsaa = "Sin salsa"
        elif salsaa == "CS":
            self.salsaa = "Con salsa"
        elif salsaa == "ES":
            self.salsaa = "Extra salsa"

    def add_esp(self, esp):
        self.especificaciones.append(esp)

    def get_esp(self) -> Pizza:
        pizza = Pizza(self.especificaciones, self.tamanioo, self.salsaa, self.quesoo)
        self.reset()
        return pizza
    
class ConcreteBuilder(Builder):
    def build_pizza_hawaiana(self):
        self.add_esp("Jamoncito")
        self.add_esp("Pinia")
        self.add_esp("chile")

    def buid_pizza_stevie(self):
        self.add_esp("Pan")
    
    def build_pizza_peperoni(self):
        self.add_esp("peperoni")

    def build_pizza_cubana(self):
        self.add_esp("Peperoni")
        self.add_esp("Jamoncito")
        self.add_esp("Pinia")
        self.add_esp("chile")
        self.add_esp("Camaron")
        self.add_esp("Pollo a la pepito")

class Director:
    def __init__(self, Builder):
        self.builder = Builder

    def construct_pizza(self):
        self.builder.build_pizza_peperoni()


builder = ConcreteBuilder("N","SS", "EQ")
director = Director(builder)
director.construct_pizza()
pizza = builder.get_esp()
pizza.show()