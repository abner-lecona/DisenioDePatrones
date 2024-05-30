def mi_funcion(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items(): # Items es para iterar en cada elemento
        print(f'{key}: {value}')

mi_funcion(1, 2, 3, 4, 5, nombre='Juan', apellido='Perez')
mi_lista = [1, 2, 3, 4, 5]
mi_diccionario = {'nombre': 'Juan', 'apellido': 'Perez'}
mi_funcion(*mi_lista, **mi_diccionario) # Necesitamos ponerle los * y ** para que se desempaquete

# Funciones como argumentos
def suma(a, b):
    return a + b

def calcula(func, a, b):
    return func(a, b)

print(calcula(suma, 10, 20))

# Regresar funciones
def saludos(nombre):
    def hello():
        return 'Hello ' + nombre
    return hello

saludo = saludos('Juan')
print(saludo())

#codigo Decorador
def make_pretty(func):
    def inner():
        print("Me hago bonito")
        func()
    return inner

@make_pretty
def ordinary():
    print('I am ordinary')

ordinary()
# decorated_ordinary = make_pretty(ordinary)
# decorated_ordinary()

def smart_divide(func):
    def inner(a,b):
        print(f"Voy a dividir {a} entre {b}")
        if b == 0:
            print("No se puede dividir entre 0")
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a , b):
    return a / b

divide(2,2)
