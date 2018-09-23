from models.Grafo import Grafo
def guardarGrafo(grafo,nombreArchivo):
    try:
        archivo = open(nombreArchivo,'w')
        for key in grafo.aristas:
            linea = ""
            linea += key
            for adyacente in grafo.aristas[key]:
                linea+= ",%s" % adyacente
            linea += '\n'
            archivo.write(linea)

        archivo2 = open("pesos."+nombreArchivo,'w')

        for key in grafo.pesos:
            linea = ""
            linea += key
            linea += "," + str(grafo.pesos[key])
            linea += "\n"
            archivo2.write(linea)
    except:
        print("Error al leer el archivo.")
    finally:
        archivo.close()
        archivo2.close()
if __name__ == "__main__":
    grafo = Grafo()
    grafo.aristas['A'] = ['B', 'C']
    grafo.pesos['AB'] = 4
    grafo.pesos['AC'] = 5
    grafo.aristas['B'] = ['D']
    grafo.pesos['BD'] = 1
    grafo.aristas['C'] = []
    grafo.aristas['D'] = ['A']
    grafo.pesos['DA'] = 3
    guardarGrafo(grafo,"prueba1.csv")