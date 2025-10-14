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


#ESTO DE AQUÍ ES TEMPORAL. Lo trabajaremos después en el main para crear las vistas del grafo y eso
if __name__ == "__main__":
    grafo = Grafo()
    grafo.extremosPorArista()
    grafo.dibujarGrafo()
    arbolRecubridorBFS = grafo.BFS("A")
    print(f"Aristas del árbol BFS: {arbolRecubridorBFS}")