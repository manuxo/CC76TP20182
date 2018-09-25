import matplotlib.pyplot as plt
from random import randint
from lee import leerDataSet,leeLA
from generarGrafo import generarGrafo
from escribe import guardarGrafo
from ucs import ucs
#Config mapa
plt.figure(figsize=(15,5))
plt.title("Mapa")
plt.xlabel("Coord X")
plt.ylabel("Coord Y")
#Pintando mapa
d = leerDataSet("dataset.csv")
x = []
y = []
for key in d:
    x.append(d[key].coordX)
    y.append(d[key].coordY)
plt.plot(x,y,'ro')
#Generando grafo y archivos

grafo = leeLA("grafo.csv")
#grafo = generarGrafo(d)
#guardarGrafo(grafo,"grafo.csv")
def generarCaminos(diccionario,grafo):
    n = len(diccionario)
    codigos = list(diccionario)
    colores = ['b','c','m','y','w']
    print("Generando caminos con UCS")
    for i in range(4):
        indiceCP = randint(0,n-1)
        codigo = codigos[indiceCP]
        costo,camino = ucs(grafo,codigo,codigo) #inicia y termina en la misma ciudad (codigo inicio y fin)
        nCoord = len(camino)
        x1 = [0]*nCoord
        y1 = [0]*nCoord
        if costo and camino:
            j = 0
            for codigoCP in camino:
                x1[j] = diccionario[codigoCP].coordX
                y1[j] = diccionario[codigoCP].coordY
                nombreCP = diccionario[codigoCP].nombre
                plt.text(x1[j], y1[j], nombreCP, family="sans-serif", color=colores[i])
                j+=1
            plt.text(x1[0], y1[0] + 0.5, str(round(costo,2)), family="sans-serif", color=colores[i])
            plt.plot(x1,y1,color=colores[i],marker="8",markerEdgeColor="black")
        else:
            continue
generarCaminos(d,grafo)
plt.show()