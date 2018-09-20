from models.CentroPoblado import CentroPoblado


def imprimeCentrosPoblados(d):
    for key in d:
        print("%s : %s" % (key,d[key]))

def leerDataSet(path):
    vertices = {}
    file = open(path)
    i = 0
    for line in file:
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
            vertices[codigoCP] = CentroPoblado(codigoCP,nombreCP,coordX,coordY)
    return vertices

if __name__ == "__main__":
    vertices = leerDataSet("dataset.csv")
    imprimeCentrosPoblados(vertices)