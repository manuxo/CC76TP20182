from models.Grafo import Grafo
from random import randint,choice
from math import sqrt,pow
from lee import leerDataSet,leeLA
from escribe import guardarGrafo

def distancia(x1,y1,x2,y2):
    return sqrt(pow(x2-x1,2) + pow(y2-y1,2))

def generarGrafo(centrosPoblados):
    grafo = Grafo()
    listaDeKeys = list(centrosPoblados)
    n = len(centrosPoblados)
    c = 0
    for key in centrosPoblados:
        codigoCP = centrosPoblados[key].codigo
        nVecinos = randint(0,10)
        vecinos = [None] * nVecinos
        for i in range(nVecinos):
            keyAleatorio = choice(listaDeKeys)
            vecinos[i] = centrosPoblados[keyAleatorio].codigo
            x1 = centrosPoblados[key].coordX
            x2 = centrosPoblados[keyAleatorio].coordX
            y1 = centrosPoblados[key].coordY
            y2= centrosPoblados[keyAleatorio].coordY
            peso = distancia(x1,x2,y1,y2)
            grafo.pesos[(key+keyAleatorio)] = peso
        grafo.aristas[codigoCP] = vecinos
        p = (c/float(n)) * 100
        print("Generando grafo(" + str(round(p,2)) + '%)')
        c+=1
    return grafo

if __name__ == "__main__":
    #grafo = generarGrafo(leerDataSet("dataset.csv"))
    grafo = leeLA("grafo")
    guardarGrafo(grafo,"copia_grafo")
