from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Beverage():
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

class CondimentDecorator(Beverage):
    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# TIPO DE CAFE
class Espresso(Beverage):
    def cost(self):
        return 1
    
    def getDescription(self):
        return 'Espresso'
    
class Decaf(Beverage):
    def cost(self):
        return 2
    
    def getDescription(self):
        return 'Decaf'
    
class DarkRoast(Beverage):
    def cost(self):
        return 3
    
    def getDescription(self):
        return 'DarkRoast'
    
class HouseBlend(Beverage):
    def cost(self):
        return 4
    
    def getDescription(self):
        return 'HouseBlend'
    
# ADITIVOS
    
class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost() + 0.5
    
    def getDescription(self):
        return self.beverage.getDescription() + ' with Mocha,'
    
class Soy(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost() + 0.5
    
    def getDescription(self):
        return self.beverage.getDescription() + ' with Soy,'
    
class Whip(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost() + 0.5
    
    def getDescription(self):
        return self.beverage.getDescription() + ' with Whip,'
    
class Milk(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost() + 0.5
    
    def getDescription(self):
        return self.beverage.getDescription() + ' with Milk,'
    
espresso = Espresso()
espresso_leche = Milk(espresso)
print(espresso_leche.cost())
print(espresso_leche.getDescription())
print()
decaf = Decaf()
decaf_leche = Milk(decaf)
print(decaf_leche.cost())
print(decaf_leche.getDescription()) 
print()
darkRoast = DarkRoast()
darkRoast_full = Milk(Mocha(Soy(Whip(darkRoast))))
print(darkRoast_full.cost())
print(darkRoast_full.getDescription())