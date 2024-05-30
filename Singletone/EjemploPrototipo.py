class Ejemplo:
    contador = 0 # Variable de clase
    def __init__(mi_instancia, valor):
        mi_instancia.valor = valor # Variable de instancia
        Ejemplo.contador += 1

    def mostrar_valor(mi_instancia):
        return f"El valor es: {mi_instancia.valor}"
    
    @classmethod
    def mostrar_contador(cls):
        return f"Contador de clase {cls.contador}"
    
    @classmethod
    def aumenta_contador(cls):
        cls.contador += 2
        return f"se sumo 2 al contador"
    
objeto1 = Ejemplo(10)
objeto2 = Ejemplo(20)
objeto3 = Ejemplo(5)

print(objeto1.mostrar_valor())
print(objeto2.mostrar_valor())
print(Ejemplo.mostrar_contador())
print(Ejemplo.aumenta_contador())
print(Ejemplo.mostrar_contador())