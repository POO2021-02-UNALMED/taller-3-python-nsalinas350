class Marca:
    def __init__(self,nombre):
        self._nombre = nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getMarca(self):
        return self._nombre