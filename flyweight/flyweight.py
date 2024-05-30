import json

# caracteristicas intrinsecas (que no cambian)
class TypeTree:
    # flyweight
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture

    def display(self, x, y, size):
        # Representa el arbol en la pantalla
        print(
            f"Mostrando un {self.name} de tamanio {size}, en la posicion ({x}, {y}) con color {self.color} y textura {self.texture}"
        )


class Tree:
    def __init__(self, x, y, size, type_tree):
        self.x = x
        self.y = y
        self.size = size
        self.type_tree = type_tree

    def display(self):
        self.type_tree.display(self.x, self.y, self.size)


class TreeFactory:
    _tree_types = {}

    @classmethod
    def get_tree_type(cls, name, color, texture):
        key = json.dumps([name, color, texture])
        if not cls._tree_types.get(key):
            print(f"Creando un nuevo tipo de arbol: {name}, {color}, {texture}")
            cls._tree_types[key] = TypeTree(name, color, texture)
        else:
            print(f"Usamos un arbol existente")
        return cls._tree_types[key]

tf = TreeFactory()
tree_type_1 = tf.get_tree_type("Pino", "Verde", "TexturaPino.jpg")
tree_type_2 =tf.get_tree_type("Jacaranda", "Morada", "TexturaJacaranda.jpg")

trees = [
    Tree(1, 1, 10, tree_type_1),
    Tree(2, 2, 20, tree_type_2)
]

for tree in trees:
    tree.display()