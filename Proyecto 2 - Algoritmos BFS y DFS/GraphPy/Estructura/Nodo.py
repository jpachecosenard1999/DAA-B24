from GraphPy.Estructura.Arista import Arista
import random
class Nodo:

    def __init__(self, nombre, geo = False):
        '''
        :param nombre: nombre del nodo
        :param geo: si es verdadero inicializa las cordenadas X y Y
        '''
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
    
    def __hash__(self):
        # El valor hash se basa en el atributo 'nombre'
        return hash(self.nombre)
    
    def __lt__(self, other):
        # Define comparación basada en el nombre del nodo
        return self.nombre < other.nombre

    def __repr__(self):
        # Representación amigable para imprimir el Nodo
        return f"Nodo({self.nombre})"
    
    def deg(self):     
        '''
        Devuelve el grado del nodo
        '''
        return len(self.listaAdyacencia)

