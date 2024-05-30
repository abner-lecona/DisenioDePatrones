from abc import ABC, abstractmethod

class IObservable(ABC):

    @abstractmethod
    def suscribe(self, observer):
        pass

    def unsuscribe(self, observer):
        pass

    def notify(self):
        pass

class Observable(IObservable):

    def __init__(self):
        self._observers = set()
    def suscribe(self, observer):
        self._observers.add(observer)
    def unsuscribe(self, observer):
        self._observers.remove(observer)
    def notify(self, *args, **kwargs): # *Args, **kwargs are optional arguments that can be passed to the observer update method 
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)

class EstacionMeteorologica(Observable):

    def __init__(self, clima):
        super().__init__()
        self._clima = clima
    def cambiaClima(self, nuevoClima, **kwargs):
        self._clima = nuevoClima
        self.notify(self._clima, **kwargs)
    

class IObserver(ABC):

    @abstractmethod
    def notify(self, observable, *args, **kwargs):
        pass

class Observer(IObserver):

    def __init__(self, nombre, observable):
        self.nombre = nombre
        observable.suscribe(self)
    def notify(self, *args, **kwargs):
        print(f'{self.nombre} ha sido notificado con el cambio de clima a: {args} {kwargs}')

class DispositivoAlerta(Observer):

    def __init__(self, nombre, observable):
        self.nombre = nombre
        super().__init__( nombre, observable)
    def notify(self, observable, *args, **kwargs):
        super().notify(*args, **kwargs)
    

estacion = EstacionMeteorologica('soleado')
appClima = DispositivoAlerta('weatherApp', estacion)
tvAzteca = DispositivoAlerta('Azteca', estacion)
estacion.cambiaClima('nublado', temperatura = 35)
estacion.cambiaClima('lluvioso', humedad = 90)


