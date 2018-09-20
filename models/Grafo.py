class Grafo:
    def __init__(self):
        self.aristas = {}
        self.pesos = {}
    def getVecinos(self, codigoCP):
        return self.aristas[codigoCP]
    def getPeso(self,origen,destino):
        return self.pesos[origen.codigo + destino.codigo]

    def agregarArista(self,centroPoblado,vecinos):
        if not centroPoblado.codigo in self.aristas.keys():
            self.aristas[centroPoblado.codigo] = []
        for vecino in vecinos:
            if not vecino.codigo in self.aristas.keys():
                self.aristas[vecino.codigo] = []
            self.aristas[centroPoblado.codigo].append(vecino)
            self.aristas[vecino.codigo].append(centroPoblado)
    
    def __str__(self):
        s = ""
        for k in self.aristas:
            s += k + " " + str(self.aristas[k])
        return s