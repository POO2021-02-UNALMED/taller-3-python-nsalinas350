class TV:
    _numTV = 0 # Atributo de clase
    #Inicializadores de atributos de instancia:
    _canal = 1
    _precio = 500
    _volumen = 1
    _control = None

    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado
        self._numTV += 1

    #gets() y sets()
    def getNumTV(self):
        return self._numTV

    @classmethod
    def setNumTV(cls,num):
        cls._numTV = num

    def getMarca(self):
	    return self._marca
    def setMarca(self,marca):
        self._marca = marca
	
    def getControl(self):
        return self._control
    def setControl(self,control):
        self._control = control

    def getPrecio(self):
        return self._precio
    def setPrecio(self, precio):
        self._precio = precio
        
    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        self._volumen = volumen
        if self._estado == False:
            return
        if(volumen>7 or volumen<0):
            return
        self._volumen = volumen
	
    def getCanal(self):
        return self._canal
    def setCanal(self,canal):
        if self._estado == False:
            return
        if(canal>120 or canal<1):
            return
        self._canal = canal
	
    #Prendido y apagado:
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado

    #Cambio de canales y volumen:
    def canalUp(self):
        if self.getEstado() == False:
            return
        if self._canal<120:
            self._canal += 1
    def canalDown(self):
        if self.getEstado() == False:
            return
        if self._canal>1:
            self._canal -= 1
	
    def volumenUp(self):
        if self.getEstado() == False:
            return
        if self._volumen<7:
            self._volumen += 1
    def volumenDown(self):
        if self.getEstado() == False:
            return
        if self._volumen>0:
            self._volumen -= 1
