from GraphPy.Arista import Arista
from GraphPy.Nodo import Nodo
import graphviz

class Grafo:

    def __init__(self, nombre, dir = False, geo = False):
        self.nombre = nombre
        self.nodos = []
        self.dir = dir
        self.geo = geo

    def AgregarNodo(self, nombreNodo):
        if(self.geo == False):
            nuevoNodo = Nodo(nombreNodo)
            self.nodos.append(nuevoNodo)
        elif(self.geo == True):
            nuevoNodo = Nodo(nombreNodo, self.geo)
            self.nodos.append(nuevoNodo)
            
        
    def AgregarNodo(self, nuevoNodo):
        self.nodos.append(nuevoNodo)
        
    def EliminarNodo(self, nodo):
        self.nodos.remove(nodo)
        
    def BuscarNodo(self, nombreNodo):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                if(nodo.nombre == nombreNodo):
                    return True
        return False
    
    def BuscarNodo(self, nodo):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                if(nodo == nodo):
                    return True
        return False
                
    def AgregarArco(self, nodoOrigen, nodoDestino, peso = 0):
        if((isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo)) and self.BuscarNodo(nodoOrigen) and self.BuscarNodo(nodoDestino)):
            arco = Arista(nodoOrigen, nodoDestino, peso)
            nodoOrigen.listaAdyacencia.append(arco)
            return True
        return False
    
    def BuscarArco(self, arco):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista)):
                        if(adyacentes == arco):
                            return nodo
        return None
    
    def ExisteArco(self, arco):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista)):
                        if(adyacentes == arco):
                            return True
        return False
    
    def EliminarArco(self, arco):
        if(isinstance(arco, Arista)):
            nodo = self.BuscarArco(arco)
            if(isinstance(nodo, Nodo)):
                nodo.listaAdyacencia.remove(arco)
                return True
        return False
    
    def Guardar(self):
        dot = graphviz.Graph(self.nombre)
        if(self.dir == True):
            dot = graphviz.Digraph(self.nombre)
        
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                dot.node(nodo.nombre, nodo.nombre)
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista) and isinstance(adyacentes.nodoOrigen, Nodo) and isinstance(adyacentes.nodoDestino, Nodo)):
                        dot.edge(adyacentes.nodoOrigen.nombre, adyacentes.nodoDestino.nombre)
        
        #dot.save(str(self.nombre) + ".gv")
        
        dot.format = "png"
        
        dot.render(directory='Grafos').replace('\\', '/')
        
    def MostrarGrafo(self):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                print("Nodo: " + nodo.nombre)
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista) and isinstance(adyacentes.nodoOrigen, Nodo) and isinstance(adyacentes.nodoDestino, Nodo)):
                        print("Arista: " + adyacentes.nodoOrigen.nombre + "-" + adyacentes.nodoDestino.nombre)
        
    