from televisores.tv import TV


from televisores.tv import TV

class Control:
    _tv = TV

    #get() y set():
    def getTv(self):
        return self._tv
    def setTv(self , tv):
        self._tv = tv

    #Método enlazar:
    def enlazar(self , tv):
        self._tv = tv
        tv._control = self

    #Acceso remoto:
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()
    def volumenDown(self):
        self._tv.volumenDown()           