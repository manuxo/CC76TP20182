from lee import leerDataSet,imprimeCentrosPoblados,CentroPoblado
from models.Grafo import Grafo

if __name__ == "__main__":
    vertices = leerDataSet("dataset.csv")
    g = Grafo()
    g.agregarArista(vertices['683908'], [
        vertices['683909'],
        vertices['683907']
    ])
    print(vertices['683908'])
    print(vertices['683907'])
    print(vertices['683909'])
    print(g)
