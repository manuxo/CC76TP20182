from models.CentroPoblado import CentroPoblado
from models.Grafo import Grafo
def leerDataSet(nombreArchivo): #retorna un diccionario de los centros poblados
    vertices = {}
    try:
        archivo = open(nombreArchivo)
        i = 0
        for line in archivo:
            if i == 0:
                i += 1
                continue
            else:
                try:
                    registro = line.split(',')
                    codigoCP = registro[4]
                    nombreCP = registro[5]
                    coordX = float(registro[15])
                    coordY = float(registro[16])
                except:
                    continue
                vertices[codigoCP] = (CentroPoblado(codigoCP,nombreCP,coordX,coordY))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
    return vertices

def leeLA(nombreArchivo): #retorna un grafo
    grafo = Grafo()
    try:
        archivoAristas = open(nombreArchivo,'r')
        lineas = archivoAristas.readlines()
        for linea in lineas:
            linea = linea.replace('\n','')
            codigos = linea.split(',')
            nodo = codigos.pop(0)
            vecinos = codigos
            grafo.aristas[nodo] = vecinos
        archivoPesos = open("pesos."+nombreArchivo)
        for linea in archivoPesos:
            valores = linea.split(',')
            arista = valores[0]
            peso = float(valores[1])
            grafo.pesos[arista] = peso
    except FileNotFoundError:
        print("Archivo no encontrado, el formato es: 'pesos.nombreArchivo' y 'nombreArchivo")
    finally:
        archivoPesos.close()
        archivoAristas.close()
    return grafo

if __name__ == "__main__":
    vertices = leerDataSet("dataset.csv")
    for k in vertices:
        print(vertices[k])
    n = len(vertices)
    print("%s elementos." % str(n))