class Arista:

    def __init__(self, nodoOrigen, nodoDestino, peso = 0):
        '''
        Clase Arista
        :param nodoOrigen: nodo origen de la arista
        :param nodoDestino: nodo destino de la arista
        :param peso: peso de la arista
        '''
        self.nodoOrigen = nodoOrigen
        self.nodoDestino = nodoDestino
        self.peso = peso
        
    def __eq__(self, other):
        if isinstance(other, Arista):
            # Considera las aristas iguales si conectan los mismos nodos
            return (self.nodoOrigen == other.nodoOrigen and self.nodoDestino == other.nodoDestino) or (self.nodoOrigen == other.nodoOrigen and self.nodoDestino == other.nodoDestino)
        return False

    def __hash__(self):
        # Implementa hash para que las aristas puedan ser utilizadas en sets o como claves de diccionario
        return hash((min(self.nodoOrigen, self.nodoDestino), max(self.nodoOrigen, self.nodoDestino)))

