from GraphPy.Arista import Arista
from GraphPy.Nodo import Nodo
import graphviz

class Grafo:

    def __init__(self, nombre, dir = False, geo = False):
        '''
        Clase Grafo
        :param nombre: nombre del grafo
        :param dir: es dirigido o no
        :param geo: es geográfico o no
        '''
        self.nombre = nombre
        self.nodos = []
        self.aristas = []
        self.dir = dir
        self.geo = geo

    def AgregarNodo(self, nombreNodo):
        '''
        Agrega un nuevo nodo al grafo por nombre. Si es geográfico pide al nodo que inicialice las coordenadas X y Y
        :param nombreNodo: nombre del nodo a crear
        '''
        if(self.geo == False):
            nuevoNodo = Nodo(nombreNodo)
            self.nodos.append(nuevoNodo)
        elif(self.geo == True):
            nuevoNodo = Nodo(nombreNodo, self.geo)
            self.nodos.append(nuevoNodo)
            
        
    def AgregarNodo(self, nuevoNodo):
        '''
        Agrega un nuevo nodo al grafo dando por párametro el nodo a añadir.
        :param nuevoNodo: nodo a añadir al grafo
        '''
        self.nodos.append(nuevoNodo)
        
    def EliminarNodo(self, nodo):
        '''
        Elimina un nodo del grafo
        :param nodo: nodo a eliminar
        '''
        self.nodos.remove(nodo)
        
    def BuscarNodo(self, nombreNodo):
        '''
        Busca un nodo por su nombre, si le encuentra retorna verdadero sino falso
        :param nombreNodo: nombre del nodo a buscar
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                if(nodo.nombre == nombreNodo):
                    return True
        return False
    
    def BuscarNodo(self, nodo):
        '''
        Busca un nodo dado, si le encuentra retorna verdadero sino falso
        :param nodo: nodo a buscar
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                if(nodo == nodo):
                    return True
        return False
                
    def AgregarArco(self, arco):
        '''
        Agrega una arista al grafo. Retorna veredadero si fue añadida sino falso
        :param arco: arista a añadir
        '''
        if(isinstance(arco, Arista) and (isinstance(arco.nodoOrigen, Nodo) and isinstance(arco.nodoDestino, Nodo)) and self.BuscarNodo(arco.nodoOrigen) and self.BuscarNodo(arco.nodoDestino)):
            arco.nodoOrigen.listaAdyacencia.append(arco)
            self.aristas.append(arco)
            return True
        return False
    
    def BuscarArco(self, arco):
        '''
        Busca una arista dada. Si lo encuentra retorna el nodo origen sino retorna None
        :param arco: arista a buscar
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista)):
                        if(adyacentes == arco):
                            return nodo
        return None
    
    def ExisteArco(self, arco):
        '''
        Combrueba si existe una arista en el grafo. Retorna verdadero si la encuentra sino falso.
        :param arco: arista a encontrar.
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista)):
                        if(adyacentes == arco):
                            return True
        return False
    
    def EliminarArco(self, arco):
        '''
        Elimina una arista del grafo. Retorna verdadero si la elimina sino retorna falso.
        :param arco: arista a eliminar.
        '''
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
            if self.dir:
                file.write("digraph G {\n")
                conector = " -> "
            else:
                file.write("graph G {\n")
                conector = " -- "
                
            # Escribir todos los nodos, incluso los que no están conectados
            for nodo in self.nodos:
                if isinstance(nodo, Nodo):
                    file.write(f'    "{nodo.nombre}";\n')  # Escribimos cada nodo por separado

            # Conjunto para evitar duplicados en grafos no dirigidos
            aristas_exportadas = set()

            for nodo in self.nodos:
                if isinstance(nodo, Nodo):
                    for adyacentes in nodo.listaAdyacencia:
                        if isinstance(adyacentes, Arista):
                            nodoOrigen = adyacentes.nodoOrigen
                            nodoDestino = adyacentes.nodoDestino
                            if isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo):
                                # Si es un grafo no dirigido, verificamos si ya se exportó la arista inversa
                                if not self.dir:
                                    if (nodoDestino.nombre, nodoOrigen.nombre) in aristas_exportadas:
                                        continue  # Ya se exportó el inverso, lo omitimos
                                    # Añadimos la arista actual al conjunto
                                    aristas_exportadas.add((nodoOrigen.nombre, nodoDestino.nombre))
                            
                                # Escribir la arista en formato GraphViz
                                file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}";\n')

            file.write("}\n")

        print(f"Grafo exportado a {filename} en formato GraphViz.")


        
    def MostrarGrafo(self):
        '''
        Muestra el grafo en la consola
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                print("Nodo: " + nodo.nombre)
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista) and isinstance(adyacentes.nodoOrigen, Nodo) and isinstance(adyacentes.nodoDestino, Nodo)):
                        print("Arista: " + adyacentes.nodoOrigen.nombre + "-" + adyacentes.nodoDestino.nombre)
        
    