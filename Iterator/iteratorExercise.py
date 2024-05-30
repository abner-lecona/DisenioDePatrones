class CadenaReversa:
    def __init__(self, cadena):
        self.cadena = cadena 
        self.caracter_actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.caracter_actual < len(self.cadena):
            caracter = self.cadena[len(self.cadena) - self.caracter_actual -1]
            self.caracter_actual += 1
            return caracter
        else:
            raise StopIteration


# Prueba tu implementación
cadena_reversa = CadenaReversa("¡Hola, mundo!")
for caracter in cadena_reversa:
    print(caracter,end="")
