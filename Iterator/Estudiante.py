class Estudiante:
    def __init__(self, nombre, promedio, clases):
        self.nombre = nombre
        self.promedio = promedio
        self.clases = clases

class GrupoEstudiantes:
    def __init__(self, estudiantes):
        self.estudiantes = estudiantes
        self.indice_actual = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice_actual < len(self.estudiantes):
            estudiante = self.estudiantes[self.indice_actual]
            self.indice_actual += 1
            return estudiante
        else:
            raise StopIteration
        
estudiantes = [
    Estudiante("Juan", 8.5, ["Matemáticas", "Física"]),
    Estudiante("María", 9.0, ["Química", "Biología"]),
    Estudiante("Pedro", 7.5, ["Historia", "Geografía"])
]

estudiantes_grupo = GrupoEstudiantes(estudiantes)
for estudiante in estudiantes_grupo:
    print(f"Nombre: {estudiante.nombre}, Promedio: {estudiante.promedio}, Clases: {estudiante.clases}")
    for clase in estudiante.clases:
        print(f"Clase: {clase}")