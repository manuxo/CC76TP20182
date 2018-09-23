class Grafo:
    def __init__(self):
        self.aristas = {}
        self.pesos = {}
    def vecinos(self, nodo):
        return self.aristas[nodo]
    def getPeso(self,nodoOrigen,nodoDestino):
        return self.pesos[(nodoOrigen + nodoDestino)]
    def __str__(self):
        s = ""
        for k in self.aristas:
            s += k + ": " + str(self.aristas[k])
        return s