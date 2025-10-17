from arista import Arista
import networkx as netx
import matplotlib.pyplot as mpl
from collections import deque
class Grafo:
    def __init__(self):
        self.estructura = netx.Graph()
        self.peso = {
        "a": 8,
        "b": 7,
        "c": 1,
        "d": 8,
        "e": 7,
        "f": 8,
        "g": 4
    }
        self.posicion = None
         

    def extremosPorArista(self):
        listaDeVertices = [
            ("A", "B", 8),
            ("A", "E", 4),
            ("A", "D", 5),
            ("B", "C", 3),
            ("B", "E", 4),
            ("C", "F", self.peso["d"] + self.peso["g"]),
            ("C", "G", self.peso["a"]),
            ("D", "E", 1),
            ("D", "I", 2),
            ("D", "H", 3),
            ("E", "F", 3),
            ("E", "I", 2),
            ("F", "G", 1),
            ("F", "K", self.peso["e"] + self.peso["f"] + self.peso["g"]),
            ("F", "I", 3),
            ("G", "L", self.peso["d"]),
            ("G", "K", self.peso["b"]),
            ("I", "K", self.peso["b"] + self.peso["c"]),
            ("I", "N", 2),
            ("I", "M", self.peso["b"] + self.peso["f"]),
            ("I", "H", self.peso["a"] + self.peso["c"]),
            ("K", "L", self.peso["e"]),
            ("K", "P", self.peso["d"]),
            ("L", "P", self.peso["f"] + self.peso["g"]),
            ("P", "N", self.peso["a"] + self.peso["b"] + self.peso["c"]),
            ("P", "I", self.peso["c"] + self.peso["e"] + self.peso["g"]),
            ("H", "M", self.peso["d"] + self.peso["g"])
        ]
        self.estructura.add_weighted_edges_from(listaDeVertices)
    
    def dibujarGrafo(self, titulo=""):
        if self.posicion == None:
            self.posicion = netx.spring_layout(self.estructura, seed=42)
        mpl.figure(figsize = (12,8))
        netx.draw(self.estructura, self.posicion, with_labels = True, node_size = 800, 
                  node_color = "darkblue", font_weight = "bold")
        labels = netx.get_edge_attributes(self.estructura, "weight")
        netx.draw_networkx_edge_labels(self.estructura, self.posicion, edge_labels = labels)
        mpl.title(titulo)
        mpl.axis("off")
        mpl.show()

    def BFS(self, verticeInicial): #recorrer al árbol en anchura
        verticesRecorridos = set()
        cadena = deque([verticeInicial])
        verticesRecorridos.add(verticeInicial)
        extremosDelArbol = []

        while cadena:
            verticeActual = cadena.popleft()
            verticesProximos = sorted(self.estructura.neighbors(verticeActual))
            for vertice in verticesProximos:
                if vertice not in verticesRecorridos:
                    verticesRecorridos.add(vertice)
                    cadena.append(vertice)
                    extremosDelArbol.append((verticeActual, vertice))

        subgrafo_BFS = netx.Graph()
        subgrafo_BFS.add_edges_from(extremosDelArbol)

        mpl.figure(figsize=(12,8))
        netx.draw(subgrafo_BFS, self.posicion, with_labels = True, node_size = 800,
                  node_color = "darkred", font_weight = "bold")
        mpl.title(f"Árbol Recubridor (BFS) desde el vértice: {verticeInicial}")
        mpl.axis("off")
        mpl.show()

        return extremosDelArbol
    def dfsrecorrer(self, verticeInicial):
        visitados = set()
        orden = []
        extremos = []

        def dfs(v):
            visitados.add(v)
            orden.append(v)
            for vecino in sorted(self.estructura.neighbors(v)):
                if vecino not in visitados:
                    extremos.append((v, vecino))
                    dfs(vecino)

        dfs(verticeInicial)

        # Crear un subgrafo con las aristas del árbol DFS
        subgrafo_DFS = netx.Graph()
        subgrafo_DFS.add_edges_from(extremos)

        if self.posicion is None:
            self.posicion = netx.spring_layout(self.estructura, seed=42)

        mpl.figure(figsize=(12,8))
        netx.draw(subgrafo_DFS, self.posicion, with_labels=True, node_size=800,
                  node_color="darkgreen", font_weight="bold")
        mpl.title(f"Árbol Recubridor (DFS) desde el vértice: {verticeInicial}")
        mpl.axis("off")
        mpl.show()

        return orden, subgrafo_DFS
    def kruskal(self):
        arbolminimo = netx.Graph()

        # Crear lista de aristas con peso
        aristas = []
        for v1, v2, peso in self.estructura.edges(data="weight"):
    
            aristas.append((v1, v2, peso))
        # Ordenar las aristas
        aristas.sort(key=lambda x: x[2])

        # Inicializar estructuras
        padres = {}
        rangos = {}

        def encontrarpadre(vertice):
            # Encontrar el padre del vertice
            if padres[vertice] != vertice:
                padres[vertice] = encontrarpadre(padres[vertice])
            return padres[vertice]

        def union(vertice1, vertice2):
            # Unir los dos vertices
            padre1 = encontrarpadre(vertice1)
            padre2 = encontrarpadre(vertice2)
            if padre1 == padre2:
                return False
            if rangos[padre1] > rangos[padre2]:
                padres[padre2] = padre1
            elif rangos[padre1] < rangos[padre2]:
                padres[padre1] = padre2
            else:
                padres[padre2] = padre1
                rangos[padre1] += 1
            return True

        # Inicializar padres y rangos
        for vertice in self.estructura.nodes():
            padres[vertice] = vertice
            rangos[vertice] = 0

        # Recorrer aristas en orden y construir árbol mínimo
        for v1, v2, peso in aristas:
            if union(v1, v2):
                arbolminimo.add_edge(v1, v2, weight=peso)

        # Dibujar árbol mínimo
        if self.posicion is None:
            self.posicion = netx.spring_layout(self.estructura, seed=42)
        mpl.figure(figsize=(12,8))
        netx.draw(arbolminimo, self.posicion, with_labels=True, node_size=800,
                  node_color="gold", font_weight="bold")
        mpl.title("Árbol Recubridor (Kruskal)")
        mpl.axis("off")
        mpl.show()

        return arbolminimo
 #ESTO DE AQUÍ ES TEMPORAL. Lo trabajaremos después en el main para crear las vistas del grafo y eso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.extremosPorArista()
    grafo.dibujarGrafo()
    arbolRecubridorBFS = grafo.BFS("A")
    print(f"Aristas del árbol BFS: {arbolRecubridorBFS}")
    arbolRecubridordfs, orden = grafo.dfsrecorrer("A")
    print(f"Orden de visita dfs: {orden}")
    arbolminimo1 = grafo.kruskal()
    print(f"Aristas del árbol minimo: {list(arbolminimo1.edges(data=True))}")
    
