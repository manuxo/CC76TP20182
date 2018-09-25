# CC76TP20182
Trabajo parcial para el curso de Complejidad Algorítmica. UPC - Universidad Peruana de Ciencias Aplicadas

## Empezando

Las siguientes instrucciones permitirán ejecutar el proyecto en su maquina local para propositos de desarrollo y pruebas

### Requisitos
  * [Python](https://www.python.org/ "Python")-> Instalar la ultima version de python disponible en el momento.
  * Libreria [Matplot](https://matplotlib.org/index.html "Matplot")-> Descargar la liberia para graficar en python, guardarla en la ruta de las demas librerias usadas.
  
### Instalacion
  1. Descargar todos los datos del repositorio.  
  
  2. Descargar la libreria [Matplot](https://matplotlib.org/index.html "Matplot")  
  
  3. Abrir nuestro editor de texto preferido para python y cargar el codigo en el.  
  
  4. Ejecutar el main.py

## Ejecutando Pruebas
En la presente seccion se indicará como realizar pruebas en el sistema

### Pruebas a realizar
El sistema permitirá cambiar la cantidad de nodos vecinos que se asignen a cada nodo principal, aunque se recomienda no hacerlo para no afectar el rendimiento.

### Ejemplos

En la funcion generarGrafo() ubicada en generarGrafo.py :

```python
def generarGrafo(centrosPoblados):
    grafo = Grafo()
    listaDeKeys = list(centrosPoblados)
    n = len(centrosPoblados)
    c = 0
    for key in centrosPoblados:
        codigoCP = centrosPoblados[key].codigo
        nVecinos = randint(0,10)
        vecinos = [None] * nVecinos
        for i in range(nVecinos):
            keyAleatorio = choice(listaDeKeys)
            vecinos[i] = centrosPoblados[keyAleatorio].codigo
            x1 = centrosPoblados[key].coordX
            x2 = centrosPoblados[keyAleatorio].coordX
            y1 = centrosPoblados[key].coordY
            y2= centrosPoblados[keyAleatorio].coordY
            peso = distancia(x1,x2,y1,y2)
            grafo.pesos[(key+keyAleatorio)] = peso
        grafo.aristas[codigoCP] = vecinos
        p = (c/float(n)) * 100
        print("Generando grafo(" + str(round(p,2)) + '%)')
        c+=1
return grafo
```
Se puede alterar el **10** de la linea con el fin de alterar numero de vecinos que tendrá cada nodo
```python 
nVecinos = randint(0,10)
```
```python 
nVecinos = randint(0,25)
```

## Autores
* [Manuel Alvarado Estanga](https://github.com/manuxo)
* [Luis Angel Bernal](https://github.com/Okotlanlais)
