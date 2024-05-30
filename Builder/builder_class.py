class Product:
    def __init__(self, parts):
        self.parts = parts

    def show(self):
        print(f"Product parts: {', '.join(self.parts)}")

class Builder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.parts = []
    
    def add_part(self, part):
        self.parts.append(part)
    
    def get_product(self) -> Product:
        product = Product(self.parts)
        self.reset()
        return product
    
class ConcreteBuilder(Builder):
    def build_part_a(self):
        self.add_part("Parte A")
    
    def build_part_b(self):
        self.add_part("Parte B")
    
    def build_part_c(self):
        self.add_part("Parte C")

class Director:
    def __init__(self, Builder):
        self.builder = Builder
    
    def construct_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

builder = ConcreteBuilder()
director = Director(builder)
director.construct_product()
product = builder.get_product()
product.show()
