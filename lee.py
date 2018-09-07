class CentroPoblado:
    def __init__(self,nombre,coordX, coordY):
        self.nombre = nombre
        self.coordX = coordX
        self.coordY = coordY

    def __str__(self):
        return "%s X: %f Y: %f" % (self.nombre,self.coordX,self.coordY)

# Dictionary
vertices = {}

def imprimeCentrosPoblados(d):
    for key in d:
        print("%s : %s" % (key,d[key]))


def leerDataSet(path):
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
            vertices[codigoCP] = CentroPoblado(nombreCP,coordX,coordY)

leerDataSet("dataset.csv")
imprimeCentrosPoblados(vertices)