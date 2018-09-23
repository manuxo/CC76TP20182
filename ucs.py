from queue import PriorityQueue
from models.Grafo import Grafo
from lee import leeLA

def ucs(grafo,inicio, meta):
    visitados = set()
    cola = PriorityQueue()
    cola.put((0,inicio,[inicio]))
    while cola:
        costo,nodo,camino = cola.get()
        if nodo not in visitados:
            visitados.add(nodo)
        for vecino in grafo.vecinos(nodo):
            costo_total = costo + grafo.getPeso(nodo,vecino)
            camino_total = camino + [vecino]
            if vecino == meta:
                return (costo_total,camino_total)
            else:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.put((costo_total,vecino,camino_total))


if __name__ == "__main__":
    grafo = leeLA("grafo")
    costo,camino = ucs(grafo,'223050','223050')
    print('Camino: ' + str(camino) + "\nCosto total: " + str(costo))
