class Iterator:
    def getNext(self):
        pass

    def hasMore(self):
        pass

class IterableColection:
    def createIterator(self):
        pass

class ListIterator(Iterator):
    def __init__(self, colection_list):
        self.colection_list = colection_list
        self.iterationState = 0

    def hasMore(self):
        if self.iterationState < len(self.colection_list):
            return True
        else:
            return False
        
    def getNext(self):
        if self.hasMore():
            item = self.colection_list[self.iterationState]
            self.iterationState += 1
            return item
        
class DictionaryIterator(Iterator):
    def __init__(self, colection_dict):
        self.colection_dict = colection_dict
        self.keys = list(colection_dict.keys())
        self.currentKey = 0
    
    def hasMore(self):
        if self.currentKey < len(self.keys):
            return True
        else:
            return False
        
    def getNext(self):
        if self.hasMore():
            key = self.keys[self.currentKey]
            value = self.colection_dict[key]
            self.currentKey += 1
            return (key, value)
        
class ListColection(IterableColection):
    def __init__(self, colection):
        self.coleccion = colection

    def createIterator(self):
        return ListIterator(self.coleccion)
        
class DictionariColection(IterableColection):
    def __init__(self, colection):
        self.coleccion = colection

    def createIterator(self):
        return DictionaryIterator(self.coleccion)

    
    
# colection_list = ListColection([1, 2, 3, 4, 5])

collectionDict = DictionariColection({1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco'})
iterator = collectionDict.createIterator()
while iterator.hasMore():
    print(iterator.getNext())
        