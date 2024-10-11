from GraphPy.Arista import Arista
from GraphPy.Nodo import Nodo
import graphviz

class Grafo:

    def __init__(self, nombre, dir = False, geo = False):
        self.nombre = nombre
        self.nodos = []
        self.aristas = []
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
                
    def AgregarArco(self, arco):
        if(isinstance(arco, Arista) and (isinstance(arco.nodoOrigen, Nodo) and isinstance(arco.nodoDestino, Nodo)) and self.BuscarNodo(arco.nodoOrigen) and self.BuscarNodo(arco.nodoDestino)):
            arco.nodoOrigen.listaAdyacencia.append(arco)
            self.aristas.append(arco)
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
        """
        Exporta el grafo en formato GraphViz (.gv) usando el nombre del grafo como nombre del archivo.
        """
        # Usamos el nombre del grafo con extensión ".gv"
        filename = self.nombre + ".gv"
    
        with open(filename, 'w') as file:
            if self.dirigido:
                file.write("digraph G {\n")
                conector = " -> "
            else:
                file.write("graph G {\n")
                conector = " -- "

            for nodo in self.nodos:
                if isinstance(nodo, Nodo):
                    for adyacentes in nodo.listaAdyacencia:
                        if isinstance(adyacentes, Arista):
                            nodoOrigen = adyacentes.nodoOrigen
                            nodoDestino = adyacentes.nodoDestino
                            if isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo):
                                # Escribir la arista en formato GraphViz
                                file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}";\n')

            file.write("}\n")

        print(f"Grafo exportado a {filename} en formato GraphViz.")

        
    def MostrarGrafo(self):
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                print("Nodo: " + nodo.nombre)
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista) and isinstance(adyacentes.nodoOrigen, Nodo) and isinstance(adyacentes.nodoDestino, Nodo)):
                        print("Arista: " + adyacentes.nodoOrigen.nombre + "-" + adyacentes.nodoDestino.nombre)
        
    