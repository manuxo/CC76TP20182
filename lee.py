from models.CentroPoblado import CentroPoblado
def leerDataSet(nombreArchivo):
    vertices = []
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
                vertices.append(CentroPoblado(codigoCP,nombreCP,coordX,coordY))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
    return vertices

if __name__ == "__main__":
    vertices = leerDataSet("dataset.csv")
    n = len(vertices)
    for i in range(n):
        print(vertices[i])