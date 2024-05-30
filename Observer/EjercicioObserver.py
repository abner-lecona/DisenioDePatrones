from abc import ABC, abstractmethod


class IObservable(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    def unsubscribe(self, observer):
        pass

    def notify(self, observer):
        pass


class Observable(IObservable):
    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    # args guarda todo como string, kwargs guarda todo como diccionario
    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(observer, *args, **kwargs)

class IObserver(ABC):
    @abstractmethod
    def notify(self, *args, **kwargs):
        pass

class Observer(IObserver):
    def __init__(self, nombre, observable):
        self.nombre = nombre
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print(f"El observer {self.nombre} recibe cambio de estatus ", args, kwargs)


class EstacionMeMeteorologia(Observable):
    def __init__(self, clima):
        self.clima = clima

    def cambiarClima(self, nuevoClima):
        self.clima = nuevoClima
        self.notify(self.clima)

class DispositivoAlerta(IObserver):
    def __init__(self, nombre):
        self.nombre = nombre

# editor = Observable()
# suscriptor = Observer("Suscriptor 1", editor)

# editor.notify("Hola suscriptores", "nuevo video", temperatura=30)
