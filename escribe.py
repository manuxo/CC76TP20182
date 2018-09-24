from models.Grafo import Grafo
def guardarGrafo(grafo,nombreArchivo):
    try:
        archivo = open(nombreArchivo,'w')
        n = len(grafo.aristas)
        c = 0
        for key in grafo.aristas:
            linea = ""
            linea += key
            for adyacente in grafo.aristas[key]:
                linea+= ",%s" % adyacente
            linea += '\n'
            archivo.write(linea)
            p = (c / float(n)) * 100
            print("Guardando aristas en: " + nombreArchivo + " (" + str(round(p,2)) + "%)")
            c +=1
        archivo2 = open("pesos."+nombreArchivo,'w')
        n = len(grafo.pesos)
        c = 0
        for key in grafo.pesos:
            linea = ""
            linea += key
            linea += "," + str(grafo.pesos[key])
            linea += "\n"
            archivo2.write(linea)
            p = (c / float(n)) * 100
            print("Guardando pesos en: pesos." + nombreArchivo + " (" + str(round(p,2)) + "%)")
            c +=1
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