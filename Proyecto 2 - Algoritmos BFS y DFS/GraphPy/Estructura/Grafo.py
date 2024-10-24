from GraphPy.Estructura.Arista import Arista
from GraphPy.Estructura.Nodo import Nodo
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
    
    def ObtenerNodo(self, nombreNodo):
        '''
        Busca un nodo por su nombre
        :param nombreNodo: nombre del nodo a buscar
        :return Nodo|None
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                if(nodo.nombre == nombreNodo):
                    return nodo
        return None
    
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

    def Cargar(self, filename: str):
        '''
        Lee el archivo gv y lo almacena en un grafo
        :param filename: nombre del archivo a cargar
        '''
        self.CargarNodos(filename)
        self.CargarAristas(filename)
        print(f"Grafo cargado desde {filename} en formato GraphViz a Grafo con nombre {self.nombre}.")

    def CargarAristas(self, filename):
        '''
        Lee el archivo gv y carga las aristas
        :param filename: nombre del archivo a cargar
        '''
        with open(filename) as archivo:
            for linea in archivo:
                if '--' in linea or '->' in linea:
                    if '--' in linea:
                        self.dir = False
                        linea_limpio = linea.replace('"', '').replace(';', '').strip()
                        extremos = linea_limpio.split('--')
                        nodoOrigen = self.ObtenerNodo(extremos[0].strip())
                        nodoDestino = self.ObtenerNodo(extremos[1].strip())
                        self.AgregarArco(Arista(nodoOrigen, nodoDestino))
                        self.AgregarArco(Arista(nodoDestino, nodoOrigen))
                    elif '->' in linea:
                        self.dir = True
                        linea_limpio = linea.replace('"', '').replace(';', '').strip()
                        extremos = linea_limpio.split('->')
                        nodoOrigen = self.ObtenerNodo(extremos[0].strip())
                        nodoDestino = self.ObtenerNodo(extremos[1].strip())
                        self.AgregarArco(Arista(nodoOrigen, nodoDestino))
        archivo.close()
                        
                    

    def CargarNodos(self, filename):
        '''
        Lee el archivo gv y carga los nodos
        :param filename: nombre del archivo a cargar
        '''
        nodos_cargados = []
        with open(filename) as archivo:
            for linea in archivo:
                if ';' in linea and '--' not in linea and '->' not in linea:
                    linea_limpio = linea.replace('"', '').replace(';', '').strip()
                    nodos_cargados.append(Nodo(linea_limpio))
        archivo.close()
        self.nodos = nodos_cargados
                    
                    
        
        
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
        
    def BFS(self, s: Nodo):
        '''
        Realiza la búsqueda a lo ancho en el grafo a partir del nodo dado y devuelve el árbol generado
        :param s: nodo a tomar como raíz
        :return árbol
        '''
        bfs = Grafo("BFS - " + self.nombre, self.dir)
        nodos_arbol = set()
        aristas_arbol = set()
        nodos_arbol.add(Nodo(s.nombre))
        visited = set()
        visited.add(s)
        parar = False
        currentlayer = set()
        currentlayer.add(s) # Al inicio se encuentra en la capa 0
        while parar == False:
            fallos = 0
            aristasRec = 0
            nextlayer = set()
            for nodos in currentlayer:
                if(isinstance(nodos, Nodo)):
                    for arcos in nodos.listaAdyacencia:
                        aristasRec = aristasRec + 1
                        if(isinstance(arcos, Arista) and arcos.nodoDestino not in visited):
                            visited.add(arcos.nodoDestino)
                            nodoA = Nodo(arcos.nodoOrigen.nombre)
                            nodoB = Nodo(arcos.nodoDestino.nombre)
                            arcoA = Arista(nodoA, nodoB)
                            arcoB = Arista(nodoB, nodoA)
                            arcoA.nodoOrigen.listaAdyacencia.append(arcoA)
                            arcoB.nodoOrigen.listaAdyacencia.append(arcoB)
                            nodos_arbol.add(nodoB)
                            nextlayer.add(arcos.nodoDestino)
                            aristas_arbol.add(arcoA)
                        else: fallos = fallos + 1
            currentlayer = nextlayer
            if(fallos == aristasRec): parar = True # Si falla en todas las aristas de la layer para porque no hay más conexiones disponibles
        
        bfs.nodos = list(nodos_arbol)
        bfs.aristas = list(aristas_arbol)
        
        
        return bfs
    
    def DFS_R(self, s):
        '''
        Realiza la búsqueda en profundidad de manera recursiva en el grafo a partir del nodo dado y devuelve el árbol generado
        :param s: nodo a tomar como raíz
        :return árbol
        '''
        dps = Grafo("DPS_R - " + self.nombre, self.dir)
        nodos_arbol = set()
        aristas_arbol = set()
        visited = set()
        visited.add(s)
        
        # Llamada inicial para explorar la raiz
        if(isinstance(s, Nodo)):
            for adyavente in s.listaAdyacencia:
                nodoDestino = adyavente.nodoDestino
                # Chequear que ningún adyacente haya sido visitado
                if(isinstance(nodoDestino, Nodo) and nodoDestino not in visited):
                    nodoA = Nodo(adyavente.nodoOrigen.nombre)
                    nodoB = Nodo(adyavente.nodoDestino.nombre)
                    arcoA = Arista(nodoA, nodoB)
                    arcoB = Arista(nodoB, nodoA)
                    arcoA.nodoOrigen.listaAdyacencia.append(arcoA)
                    arcoB.nodoOrigen.listaAdyacencia.append(arcoB)
                    nodos_arbol.add(nodoB)
                    aristas_arbol.add(arcoA)
                    
                    # Llamada al método recursivo
                    n,a = self.Call_R(nodoDestino, visited)
                    
                    # Actualizar los nodos y aristas del árbol
                    nodos_arbol.update(n)
                    aristas_arbol.update(a)
                    
        
        dps.nodos = list(nodos_arbol)
        dps.aristas = list(aristas_arbol)
        
        return dps
    
    def Call_R(self, s, visited: set):
        '''
        Método recursivo que explora los nodos que no son la raíz. Los subárboles de los nodos adyacentes
        :param s: nodo a tomar como raíz
        :return Tupla -> n: nodos del subárbol y a: aristas del subárbol
        '''
        nodos_arbol = set()
        aristas_arbol = set()
        
        if(isinstance(s, Nodo)):
            visited.add(s) # Añado la raiz del subárbol como visitada
            for adyavente in s.listaAdyacencia:
                nodoDestino = adyavente.nodoDestino
                # Chequear que ningún adyacente haya sido visitado
                if(isinstance(nodoDestino, Nodo) and nodoDestino not in visited):
                    nodoA = Nodo(adyavente.nodoOrigen.nombre)
                    nodoB = Nodo(adyavente.nodoDestino.nombre)
                    arcoA = Arista(nodoA, nodoB)
                    arcoB = Arista(nodoB, nodoA)
                    arcoA.nodoOrigen.listaAdyacencia.append(arcoA)
                    arcoB.nodoOrigen.listaAdyacencia.append(arcoB)
                    nodos_arbol.add(nodoB)
                    aristas_arbol.add(arcoA)
                    
                    # Llamada al método recursivo
                    n,a = self.Call_R(nodoDestino, visited)
                    
                    # Actualizar los nodos y aristas del árbol
                    nodos_arbol.update(n)
                    aristas_arbol.update(a)
        
        return nodos_arbol, aristas_arbol
    
    def DFS_I(self, s):
        '''
        Realiza la búsqueda en profundidad de manera iterativa en el grafo a partir del nodo dado y devuelve el árbol generado
        :param s: nodo a tomar como raíz
        :return árbol
        '''
        dps = Grafo("DPS_I - " + self.nombre, self.dir)
        nodos_arbol = set()
        aristas_arbol = set()
        visited = set()
        stack = [s] # Al inicio se encuentra el nodo inicial en la pila
        while(stack): # Mientras la pila no esté vacía
            nodo = stack.pop()
            if(isinstance(nodo, Nodo) and nodo not in visited):
                visited.add(nodo) # Marco el nodo como visitado
                # Agrego sus adyacentes a la pila
                for adyacentes in nodo.listaAdyacencia:
                    if(isinstance(adyacentes, Arista) and adyacentes not in aristas_arbol):
                        nodoA = Nodo(adyacentes.nodoOrigen.nombre)
                        nodoB = Nodo(adyacentes.nodoDestino.nombre)
                        arcoA = Arista(nodoA, nodoB)
                        arcoB = Arista(nodoB, nodoA)
                        arcoA.nodoOrigen.listaAdyacencia.append(arcoA)
                        arcoB.nodoOrigen.listaAdyacencia.append(arcoB)
                        nodos_arbol.add(nodoB)
                        stack.append(adyacentes.nodoDestino) # Añado todos los nodos adyacentes a la pila
        dps.nodos = list(nodos_arbol)
        dps.aristas = list(aristas_arbol)
        
        return dps