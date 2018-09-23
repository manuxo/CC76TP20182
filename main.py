import matplotlib.pyplot as plt
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

costo,camino = ucs(grafo,'223050','223050')

x1 = []
y1 = []
for codigoCP in camino:
    x1.append(d[codigoCP].coordX)
    y1.append(d[codigoCP].coordY)
plt.plot(x1,y1,color="green",marker="8",markerEdgeColor="blue")




plt.show()