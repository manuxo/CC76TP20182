# CC76TP20182
Trabajo parcial para el curso de Complejidad Algorítmica. UPC - Universidad Peruana de Ciencias Aplicadas

![](https://media.giphy.com/media/VD9NtdBN9CwqQ/giphy.gif)

## Introducción
A lo largo de la existencia de las computadoras, se ha considerado a estas como herramientas de las cuales nos podemos valer para facilitar nuestras actividades. Así, se ha pensado que las computadoras nos pueden ayudar a resolver todos nuestros problemas y que poseen más poder para procesar datos que nosotros. Es raro pensar en que las computadoras poseen limites en sus facultades de cálculo, ya que muy pocas veces nos encontramos ante tales limites; de hecho, probablemente el usuario promedio no tenga que lidiar nunca en su vida con ningún problema que requiera llevar el poder de procesamiento de la computadora hasta casi el límite. Pese a esto, hasta el día de hoy existen ciertos problemas que no han podido ser resueltos ni con la ayuda de las computadoras, esto se debe a que quizás si se pueda encontrar una respuesta, pero el tiempo que le llevaría a las computadoras darnos el resultado podría ser de hasta millones de años.

### P vs NP
Por esta razón se plantea el problema P vs. NP; este problema es considerado como uno de los tantos problemas del millón de dólares. Este problema consiste en comprobar que los problemas NP pueden ser resueltos de igual forma que los polinómicos(P) aplicando diversos conceptos que permitan facilitar el proceso de resolución. Este problema trata de aclarar que problemas pueden resolverse con la ayuda de la computadora y cuales no, para de esta forma determinar si la resolución de dichos problemas se hallará relacionada a la creación de equipos más con más potencia de análisis.

 - P: Las soluciones pueden ser calculadas en un tiempo razonable
 - NP: Las soluciones son muy dificiles de encontrar, pero son fáciles de comprobar

El reto es demostrar que P = NP o lo contrario; es decir, mientras no se pruebe que son diferentes podrían existir atajos que permitan resolver un problema de clase NP como uno de complejidad P. Demostrar que P = NP tendría grandes impactos en la criptografía moderna y haría vulnerables a todos los sistemas a nivel mundial en el caso que sea cierto.

![Gráfico P vs NP](https://qph.fs.quoracdn.net/main-qimg-29c826310da7fed7e085181bafc99598)

Fuente: [Quora - Does P ! = NP mean that no problem exists which can be solved and checked in polynomial time?](https://www.quora.com/Does-P-NP-mean-that-no-problem-exists-which-can-be-solved-and-checked-in-polynomial-time)

### TSP - Travelling Salesman Problem
Entre estos problemas de complejidad NP, se encuentra el problema del vendedor viajero (TSP, por sus siglas en ingles). Dada una colección de ciudades y las distancias entre sus conexiones (costo), el  problema consiste en encontrar un camino que recorra todas las ciudades una única vez y regrese al punto inicial con la menor distancia posible.
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Aco_TSP.svg/600px-Aco_TSP.svg.png)

Fuente: [Wikipedia - Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
## Objetivos

 - Desarrollar la competencia general de razonamiento cuantitativo y la competencia específica de uso de técnicas y herramientas acorde a los objetivos del curso.
 - Desarrollar un algoritmo que permita resolver completa o parcialmente el problema del vendedor viajero.
 - Establecer relaciones entre problemas de la vida diaria y problemas computacionales.
 - Determinar la importancia de la aplicación de algoritmos eficientes a la hora de resolver un problema.
 - Analizar la eficiencia y complejidad de los algoritmos planteados.

## Marco Teórico

### Búsqueda en grafos
#### Búsqueda por amplitud - BFS
Este algoritmo de búsqueda consiste en recorrer los vértices de un grafo de izquierda a derecha; es decir, en lugar de recorrer una rama hacia abajo como lo hace la búsqueda por profundidad (DFS), recorre todos los nodos que se encuentran en el mismo nivel. Una posible implementación del algoritmo es la siguiente:
```python
def  bfs(grafo,inicio,meta):
	cola = [(inicio,[inicio])]
	visitados =  set()
	while  len(cola) >  0:
		nodo,camino = cola.pop(0)
		if nodo not  in visitados:
			visitados.add(nodo)
		for vecino in grafo.vecinos(nodo):
			if vecino == meta:
				return camino + [vecino]
			else:
				if vecino not  in visitados:
					visitados.add(vecino)
					cola.append((vecino,camino+[vecino]))
	return  None
```


![](https://he-s3.s3.amazonaws.com/media/uploads/fdec3c2.jpg)
Fuente: [Hacker Earth - Breadth First Search](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/)

### Búsqueda por costo uniforme - UCS

Este algoritmo de búsqueda trabaja con grafos ponderados o con pesos. En este tipo de grafos cada vértice tiene un peso y se define el costo de la arista como la distancia entre los vértices conectados. La búsqueda se realiza a partir de un punto inicial y recorre los vértices más cercanos, de tal manera que se va acumulando el costo total. Esta estrategia utiliza una cola de prioridades (Priority Queue) la cual ordena los vértices y sus respectivos costos en pares (v,c) dentro de una colección del tipo LIFO. Este tipo de colas ubica los elementos de forma ordenada según la prioridad; es decir, los elementos con menor costo estarán ubicados al final y van a ser los primeros en  salir. Una posible implementación del algoritmo es la siguiente:

``` python

    def  ucs(grafo,inicio, meta):
	    visitados =  set()
	    cola = PriorityQueue()
	    cola.put((0,inicio,[inicio]))
	    while cola:
		    costo,nodo,camino = cola.get()
		    if nodo not  in visitados:
			    visitados.add(nodo)
		    for vecino in grafo.vecinos(nodo):
			    costo_total = costo + grafo.getPeso(nodo,vecino)
			    camino_total = camino + [vecino]
			    if vecino == meta:
				    return (costo_total,camino_total)
				else:
				    if vecino not  in visitados:
					    visitados.add(vecino)
					    cola.put((costo_total,vecino,camino_total))
	    return (None,None)
```
![](https://algorithmicthoughts.files.wordpress.com/2012/12/searchtree.png?w=348&h=364)
Fuente: [Artificial Intelligence – Uniform Cost Search (UCS)](https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/)
## Bibliografía

Jiménez, A. (2006, agosto 26). _P versus NP. ¿Nunca lo entendiste?_ Retrieved from Xataka Ciencia: https://www.xatakaciencia.com/matematicas/p-versus-np-nunca-lo-entendiste

Pavlus, J. (19 de agosto de 2010). _¿Qué significa 'P vs NP' para el resto de nosotros?_ Obtenido de MIT Technology review: https://www.technologyreview.es/s/1374/que-significa-p-vs-np-para-el-resto-de-nosotros

http://cyluun.github.io/blog/uninformed-search-algorithms-in-python

https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/

https://algorithmicthoughts.wordpress.com/2012/12/15/artificial-intelligence-uniform-cost-searchucs/
