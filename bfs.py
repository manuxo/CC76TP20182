def bfs(grafo,inicio,meta):
    cola = [(inicio,[inicio])]
    visitados = set()
    while len(cola) > 0:
        nodo,camino = cola.pop(0)
        if nodo not in visitados:
            visitados.add(nodo)
        for vecino in grafo.vecinos(nodo):
            if vecino == meta:
                return camino + [vecino]
            else:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino,camino+[vecino]))
    return None
