from GraphPy.Arista import Arista
import random
class Nodo:

    def __init__(self, nombre, geo = False):
        self.nombre = nombre
        self.listaAdyacencia = []
        self.X = 0
        self.Y = 0
        if(geo == True):
            self.X = random.random()
            self.Y = random.random()
    
    def __eq__(self, other):
        if isinstance(other, Nodo):
            # Considera las aristas iguales si conectan los mismos nodos
            return (self.nombre == other.nombre) or (self.nombre == other.nombre)
        return False
    
    def deg(self):
        return len(self.listaAdyacencia)

