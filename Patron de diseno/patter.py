#
# Tarea:Escribe un adaptador para el Speedometer de forma  que trabaje con la clase CarDisplay
import random


class MphSpeedometer:
    """Estamos pretendiendo que esta es una clase exerna que no podemos cambiar"""

    def __init__(self):
        pass

    def get_speed(self):
        """Regresa la velocidad en MPH (Millas por hora)"""
        speed = random.randint(0, 100)
        print("Speed in MPH: {}".format(speed))
        return speed


class MphToKphSpeedometerAdapter:
    def __init__(self):
        pass

    def get_speed(self):
        mph_speedometer = MphSpeedometer()
        speed = mph_speedometer.get_speed()
        speed = speed * 1.60934
        return speed



class CarDisplay:
    def __init__(self, speedometer):
        self.speedometer = speedometer

    def show_speed(self):
        # Mostrar la velocidad utilizando el método get_speed del adaptador
        speed = self.speedometer.get_speed()
        print(f"Speed: {speed}")

if __name__ == "__main__":
    """TAREA: cambia tanto como necesites para tu nuevo adaptador"""
    speedometer = MphSpeedometer()
    speedometer = MphToKphSpeedometerAdapter()
    car_display = CarDisplay(speedometer)
    car_display.show_speed()