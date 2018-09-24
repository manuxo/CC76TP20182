import matplotlib.pyplot as plt
import collections
from random import randint, choice
from lee import leerDataSet
from bfs import bfs
from generarGrafo import generarGrafo

#Config grafico
plt.figure(figsize=(15,5))
plt.title("Muestra de centros poblados")
plt.xlabel("Coord X")
plt.ylabel("Coord Y")
#Generando un subset de todos los centros poblados
d = leerDataSet("dataset.csv")
def sub_dict(somedict, somekeys, default=None):
    return dict([ (k, somedict.get(k, default)) for k in somekeys ])
llaves = list(d)
llavesSub = set()
nCiudades = randint(2,75)
for i in range(nCiudades):
    k = choice(llaves)
    llavesSub.add(k)
subD = sub_dict(d,llavesSub)
x = []
y = []
for key in subD:
    x.append(d[key].coordX)
    y.append(d[key].coordY)
#Pintando esa muestra de n ciudades
plt.plot(x,y,'ro')

#Generando caminos con bfs
def generarCaminos(diccionario,grafo):
    codigos = list(diccionario)
    colores = ['b','c','m','y','w']
    print("Generando caminos con BFS")
    caminos = []
    solucion = [None]*2 # [inicio,final]
    buscarCaminos(grafo,codigos,solucion,0,caminos)
    for c in caminos:
        x = []
        y = []
        colorC = colores[0]
        #Valida si el camino recorre todos los nodos
        #Lo pinta de otro color
        if collections.Counter(c) == collections.Counter(codigos):
            colorC = colores[2]
        for codigoCP in c:
            x.append(diccionario[codigoCP].coordX)
            y.append(diccionario[codigoCP].coordY)
        plt.plot(x,y,color=colorC,marker="8",markerEdgeColor="black")
#Backtracking
#solucion = [inicio,fin]
def buscarCaminos(grafo,codigos,solucion,etapa,caminos):
    n = len(solucion)
    numCentrosPoblados = len(codigos)
    if etapa > n: #No hay solución
        return
    i = 0
    while True:
        solucion[etapa] = codigos[i]
        if etapa == n-1:
            camino = bfs(grafo,solucion[0],solucion[1])
            #Validar si ha recorrido todos los nodos del grafo (codigos)
            if camino:
                caminos.append(camino)
        else:
            buscarCaminos(grafo,codigos,solucion,etapa+1,caminos)
        i+=1
        if i == numCentrosPoblados:
            break

grafo = generarGrafo(subD)
generarCaminos(subD,grafo)

a = ['a','c','b']
b = ['b','a','c']


plt.show()