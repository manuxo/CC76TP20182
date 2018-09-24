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
        n = len(lineas)
        c = 0
        for linea in lineas:
            linea = linea.replace('\n','')
            codigos = linea.split(',')
            nodo = codigos.pop(0)
            vecinos = codigos
            grafo.aristas[nodo] = vecinos
            p = (c/float(n)) * 100
            print("Leyendo aristas (" + str(round(p,2)) + "%)")
            c+=1
        archivoPesos = open("pesos."+nombreArchivo)
        lineas = archivoPesos.readlines()
        n = len(lineas)
        c = 0
        for linea in lineas:
            valores = linea.split(',')
            arista = valores[0]
            peso = float(valores[1])
            grafo.pesos[arista] = peso
            p = (c/float(n)) * 100
            print("Leyendo pesos (" + str(round(p,2)) + "%)")
            c+=1
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