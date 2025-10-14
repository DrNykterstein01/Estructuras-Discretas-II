import networkx as netx
import matplotlib as mpl


class Arista:
    def __init__(self, vertice1, vertice2, ponderacion=0):
        self.vertice1 = vertice1 #Nos identifica el primer vértice
        self.vertice2 = vertice2 #Nos identifica el segundo vértice
        self.ponderacion = ponderacion #recibirá un array con los valores a sumar
    

    