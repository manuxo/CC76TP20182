class CentroPoblado:
    def __init__(self,codigo,nombre,coordX, coordY):
        self.codigo = codigo
        self.nombre = nombre
        self.coordX = coordX
        self.coordY = coordY

    def __str__(self):
        return "%s Cod: %s  X: %f Y: %f" % (self.nombre, self.codigo,self.coordX,self.coordY)