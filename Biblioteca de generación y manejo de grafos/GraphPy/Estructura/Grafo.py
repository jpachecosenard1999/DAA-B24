from GraphPy.Estructura.Arista import Arista
from GraphPy.Estructura.UnionFind import UnionFind
from GraphPy.Estructura.Nodo import Nodo
import graphviz
import random
import heapq
import re
import pygame
import math
import cv2
import numpy as np

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
            
        
    def AgregarNodo(self, nuevoNodo: Nodo):
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
                                if(adyacentes.peso == 0):
                                    file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}";\n')
                                else:
                                    label = '[label=' + str(adyacentes.peso) + ']'
                                    file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}"{label};\n')

            file.write("}\n")

        print(f"Grafo exportado a {filename} en formato GraphViz.")
                  

    def GuardarConEtiquetasYColor(self, camino_resaltado = set(), last = ""):
        """
        Exporta el grafo en formato GraphViz (.gv), resaltando nodos específicos y coloreando un camino dado.
        """
        # Nombre del archivo .gv
        filename = self.nombre + ".gv"

        # Patrón de regex para detectar nodos que deben tener etiqueta
        #patron_nodo_resaltado = re.compile(r'N-\d+\(\d+\.\d+\)')
        #patron_nodo_inicio = re.compile(r"N-0(?:,0)?")  # Detecta "N-0" o "N-0,0"

        with open(filename, 'w') as file:
            if self.dir:
                file.write("digraph G {\n")
                conector = " -> "
            else:
                file.write("graph G {\n")
                conector = " -- "

            # Escribir todos los nodos, aplicando etiquetas a los resaltados
            for nodo in self.nodos:
                if isinstance(nodo, Nodo): 
                    if nodo.nombre == last:
                        # Resalta nodos que cumplen con el patrón
                        file.write(f'    "{nodo.nombre}" [label="{nodo.nombre}",color=red, fontcolor=red, style=filled, fillcolor=red];\n')
                    else:
                        # Nodo sin resaltado
                        file.write(f'    "{nodo.nombre}";\n')

            # Conjunto para evitar duplicados en grafos no dirigidos
            aristas_exportadas = set()

            for nodo in self.nodos:
                if isinstance(nodo, Nodo):
                    for adyacentes in nodo.listaAdyacencia:
                        if isinstance(adyacentes, Arista):
                            nodoOrigen = adyacentes.nodoOrigen
                            nodoDestino = adyacentes.nodoDestino
                            if isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo):
                                # Evitar duplicados si el grafo es no dirigido
                                if not self.dir:
                                    if (nodoDestino.nombre, nodoOrigen.nombre) in aristas_exportadas:
                                        continue
                                    aristas_exportadas.add((nodoOrigen.nombre, nodoDestino.nombre))

                                # Escribir la arista en el archivo, con o sin estilo
                                if nodo.nombre in camino_resaltado:
                                    file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}" [color=red, penwidth=2, weight=2];\n')
                                else:
                                    file.write(f'    "{nodoOrigen.nombre}"{conector}"{nodoDestino.nombre}" [color=black, penwidth=2, weight=2];\n')

            file.write("}\n")

        print(f"Grafo exportado a {filename} con etiquetas y camino resaltado en formato GraphViz.")

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
                    
    def AsignarPeso(self):
        '''Asigna Peso a las Aristas'''
        if(self.dir == True):
            for nodo in self.nodos:
                if(isinstance(nodo, Nodo)):
                    for adyacentes in nodo.listaAdyacencia:
                        if(isinstance(adyacentes, Arista) and isinstance(adyacentes.nodoOrigen, Nodo) and isinstance(adyacentes.nodoDestino, Nodo)):
                            adyacentes.peso = random.random() * 100 # Obtengo un valor random y lo multiplico por 100 para escalar
        else:
            for nodo in self.nodos:
                if isinstance(nodo, Nodo):
                    for adyacente in nodo.listaAdyacencia:
                        if(isinstance(adyacente, Arista) and isinstance(adyacente.nodoOrigen, Nodo) and isinstance(adyacente.nodoDestino, Nodo)):
                            # Si la arista no tiene peso, asignamos uno nuevo
                            if adyacente.peso == 0:
                                nuevo_peso = random.random() * 100
                                adyacente.peso = nuevo_peso # Obtengo un valor random y lo multiplico por 100 para escalar
                        
                                # Encontrar y asignar el mismo peso a la arista inversa
                                nodo_destino = adyacente.nodoDestino
                                for arista_inversa in nodo_destino.listaAdyacencia:
                                    if(isinstance(arista_inversa, Arista) and
                                        arista_inversa.nodoDestino == nodo):
                                        arista_inversa.peso = nuevo_peso
                                        break       
    
    def AsiganarValoresXY(self):
        '''
        Asigna de manera aleatoria los valores de X y Y para ser usados en el método SPRING
        '''
        for nodo in self.nodos:
            if(isinstance(nodo, Nodo)):
                nodo.attr["X"] = random.randint(100, 700)
                nodo.attr["Y"] = random.randint(100, 500)
        
        
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
        dps = Grafo("DFS_R - " + self.nombre, self.dir)
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
        dps = Grafo("DFS_I - " + self.nombre, self.dir)
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
    
    def Dijkstra(self, s):
        '''
        Realiza el algoritmo del camino más corto en el grafo a partir del nodo dado y devuelve el árbol generado
        :param s: nodo a tomar como raíz
        :return árbol
        '''
        arbol = Grafo("Dijkstra - " + self.nombre, self.dir)
        
        distancias = {}
        predecesor = {}
        
        for nodo in self.nodos:
            distancias[nodo] = 99999999999 # Asigno un peso gigantesco
        
        distancias[s] = 0 # Asigno valor cero a la distancia del nodo inicial
        
        nodos_visitados = set()
        
        # Cola de prioridad
        pq = []
        heapq.heappush(pq, (0, s))  # (distancia, nodo)
        
        while(pq):
            # Selecciono el nodo con menor distancia
            dist_actual, nodo_actual = heapq.heappop(pq)

            if distancias[nodo_actual] == 99999999999: break # Rompo el ciclo porque el resto de nodos no son alcanzables
            
            if(isinstance(nodo_actual, Nodo)):
                for adyacentes in nodo_actual.listaAdyacencia:
                    if(isinstance(adyacentes, Arista)):
                        dist_tentativa = dist_actual + adyacentes.peso
                        if(dist_tentativa < distancias[adyacentes.nodoDestino]):
                            distancias[adyacentes.nodoDestino] = dist_tentativa
                            predecesor[adyacentes.nodoDestino] = nodo_actual
                            heapq.heappush(pq, (dist_tentativa, adyacentes.nodoDestino))

            nodos_visitados.add(nodo_actual)
            
            
        #arbol.AgregarNodo(Nodo(s.nombre))
        
        nodos_arbol = set()
        aristas_arbol = set()
        
        ultima_nodo = list(distancias.keys())[-1]
        
        nodos_arbol.add(Nodo(s.nombre))
        
        # Creación del árbol
        
        for predec in predecesor.keys():
            nodoO = Nodo(predecesor[predec].nombre)
            nodoD = Nodo(predec.nombre + "(" + str(distancias[predec]) + ")")
            arcoA = Arista(nodoO,nodoD)
            arcoB = Arista(nodoD,nodoO)
            arcoA.nodoOrigen.listaAdyacencia.append(arcoA)
            arcoB.nodoOrigen.listaAdyacencia.append(arcoB)
            if(nodoO.nombre != s.nombre):
                nodoO.nombre = nodoO.nombre + "(" + str(distancias[predecesor[predec]]) + ")"
            nodos_arbol.add(nodoD)
            aristas_arbol.add(arcoA)
        
        arbol.nodos = list(nodos_arbol)
        arbol.aristas = list(aristas_arbol)
        
        
        arbol.GuardarConEtiquetasYColor(last = s.nombre)
        
        return arbol
    
    def KruskalD(self):
        '''
        Calcula el árbol de expansión mínima mediante el Algoritmo de Kruskal (Directo)
        :return árbol
        '''
        arbol = Grafo("Kruskal-D " + self.nombre, self.dir)
    
        # Ordenar las aristas ascendentemente por peso
        sortedAristas = sorted(self.aristas, key=lambda arista: arista.peso)
    
        # Inicializar Clase Auxiliar para manejar conjuntos
        uf = UnionFind(self.nodos)
    
        valueMST = 0  # Valor del árbol de expansión mínima

        for arista in sortedAristas:
            nodoOrigen = arista.nodoOrigen
            nodoDestino = arista.nodoDestino

            if(uf.find(nodoOrigen) != uf.find(nodoDestino)):
                uf.union(nodoOrigen, nodoDestino)

                # Añadimos la arista al árbol
                nodoA = Nodo(nodoOrigen.nombre)
                nodoB = Nodo(nodoDestino.nombre)
                arcoA = Arista(nodoA, nodoB, arista.peso)
                arcoB = Arista(nodoB, nodoA, arista.peso)

                nodoA.listaAdyacencia.append(arcoA)
                nodoB.listaAdyacencia.append(arcoB)
                arbol.nodos.append(nodoA)
                arbol.nodos.append(nodoB)
                arbol.aristas.append(arcoA)

                # Actualizar el valor del árbol de expansión mínima
                valueMST += arista.peso

        valueMST = round(valueMST, 3)
        print("Valor del árbol de expansión mínima: " + str(valueMST))
        arbol.Guardar()
        return arbol
    
    def CrearArbol(self, arista_eliminar: Arista): 
        '''
        Crea un árbol sin la arista pasada por parámetro
        :param arista_eliminar: arista a excluir del árbol
        :return: arbol (subgrafo sin la arista eliminada)
        '''
        arbol = Grafo("Kruskal-I " + self.nombre, self.dir)
    
        # Diccionario con nodos del árbol
        nodo_map = {nodo.nombre: Nodo(nodo.nombre) for nodo in self.nodos}
        arbol.nodos = list(nodo_map.values())
    
        for arista in self.aristas:
            if(arista != arista_eliminar):
                nodo_origen = nodo_map[arista.nodoOrigen.nombre]
                nodo_destino = nodo_map[arista.nodoDestino.nombre]
            
                arcoA = Arista(nodo_origen, nodo_destino, arista.peso)
                arcoB = Arista(nodo_destino, nodo_origen, arista.peso)
            
                nodo_origen.listaAdyacencia.append(arcoA)
                nodo_destino.listaAdyacencia.append(arcoB)
            
                arbol.aristas.append(arcoA)
    
        return arbol

    
    def KruskalI(self):
        '''
        Calcula el árbol de expansión mínima mediante el Algoritmo de Kruskal (Inverso)
        :return árbol
        '''
        arbol = Grafo("Kruskal-I " + self.nombre, self.dir)
        arbol.nodos = self.nodos
        arbol.aristas = self.aristas
    
        # Ordenar las aristas descendentemente por peso
        sortedAristas = sorted(self.aristas, key=lambda arista: arista.peso, reverse=True)
    
        valueMST = 0 # Valor del árbol de expansión mínima
        
        # El valor inicial es la suma de todos los pesos
        for arista in self.aristas:
            valueMST += arista.peso

        for arista in sortedAristas:
            # Crear un arbol sin la arista actual
            arbol2 = arbol.CrearArbol(arista)
        
            # Ejecutar BFS desde el nodo inicial
            nodo_inicio = arbol2.nodos[0]  
            bfs_result = arbol2.BFS(nodo_inicio)
        
            # Si la cantidad de nodos visitados es igual a la cantidad de nodos totales, el grafo sigue siendo conexo
            if(len(bfs_result.nodos) == len(arbol2.nodos)):
                arbol = arbol2
                valueMST -= arista.peso
            else: continue  # Saltamos esta arista porque desconecta el árbol

        valueMST = round(valueMST, 3)
        print("Valor del árbol de expansión mínima: " + str(valueMST))
        arbol.nombre = "Kruskal-I " + self.nombre
        arbol.Guardar()
        return arbol
    
    

    def Prim(self, s: Nodo):
        """
        Calcula el árbol de expansión mínima mediante el Algoritmo de Prim.
        :param s: Nodo inicial
        :return: Grafo con el MST
        """
        # Inicializar el árbol de expansión mínima (MST)
        arbol = Grafo("Prim - " + self.nombre, self.dir)

        # Inicializar distancias a infinito para todos los nodos
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[s] = 0

        valueMST = 0
        
        visited = set()
        visitedAristas = set()
        
        # Cola de prioridad para manejar las aristas
        pq = []
        heapq.heappush(pq, (0, s, None))
        
        while pq:
            peso, nodo, previo = heapq.heappop(pq)
            
            if(nodo in visited): continue # Si ya fue visitado saltar a la siguiente iteración
            
            # Si no es el primer nodo, agregar la arista correspondiente al MST
            if previo is not None:
                # valueMST += peso  # Sumar el peso de la arista al MST
                nodoOrigen = Nodo(previo.nombre)
                nodoDestino = Nodo(nodo.nombre)
                arcoA = Arista(nodoOrigen, nodoDestino, peso)
                arcoB = Arista(nodoDestino, nodoOrigen, peso)
                nodoOrigen.listaAdyacencia.append(arcoA)
                nodoDestino.listaAdyacencia.append(arcoB)
                arbol.nodos.append(nodoOrigen)
                arbol.aristas.append(arcoA)
                # print(f"Arista seleccionada: {previo} --({peso})--> {nodo}")
                
            # Añadir el peso al MST solo si es la distancia mínima
            if peso == distancias[nodo]:
                valueMST += peso # Sumar el peso de la arista al MST
            
            visited.add(nodo) # Marco el nodo como visitado
            
            adyacentes = nodo.listaAdyacencia
            
            for ady in adyacentes: # Añado las aristas adyacentes
                if(isinstance(ady, Arista)):
                    ady_invertido = Arista(ady.nodoDestino, ady.nodoOrigen, ady.peso)
                    if(ady not in visitedAristas and ady.peso < distancias[ady.nodoDestino]):
                        visitedAristas.add(ady)
                        distancias[ady.nodoDestino] = ady.peso
                        heapq.heappush(pq, (ady.peso, ady.nodoDestino, nodo))

        
        valueMST = round(valueMST, 3)
        print(f"Valor del árbol de expansión mínima: {valueMST}")
        
        arbol.Guardar()
        return arbol
    
    # MÉTODOS PROYECTO 5
    
    def calcular_fuerzas(self, C1 = 0.0, C2 = 0.0):
        '''
        Calcula la fuerza x y fuerza y para el método Spring
        :param C1: constante de atracción
        :param C2: constante de repulsión
        '''
        # Resetear fuerzas
        for nodo in self.nodos:
            nodo.attr["fuerza_x"] = 0
            nodo.attr["fuerza_y"] = 0
        
        # Cálculo de fuerzas de repulsión
        for i, nodoOrigen in enumerate(self.nodos):
            for j, nodoDestino in enumerate(self.nodos):
                if i != j:
                    dx = nodoOrigen.attr["X"] - nodoDestino.attr["Y"]
                    dy = nodoOrigen.attr["Y"] - nodoDestino.attr["X"]
                    dist = math.sqrt(dx ** 2 + dy ** 2) or 1
                    fuerza = C2 / dist
                    nodoOrigen.attr["fuerza_x"] += fuerza * dx / dist
                    nodoOrigen.attr["fuerza_y"] += fuerza * dy / dist

        # Cálculo de fuerzas de atracción
        for arco in self.aristas:
            dx = arco.nodoOrigen.attr["X"] - arco.nodoDestino.attr["X"]
            dy = arco.nodoOrigen.attr["Y"] - arco.nodoDestino.attr["Y"]
            dist = math.sqrt(dx ** 2 + dy ** 2) or 1
            fuerza = -C1 * math.log(dist)
            arco.nodoOrigen.attr["fuerza_x"] += fuerza * dx / dist
            arco.nodoOrigen.attr["fuerza_y"] += fuerza * dy / dist
            arco.nodoDestino.attr["fuerza_x"] -= fuerza * dx / dist
            arco.nodoDestino.attr["fuerza_y"] -= fuerza * dy / dist

    def actualizar_posiciones(self, ANCHO, ALTO, C3 = 0.0):
        '''
        Actualiza las posiciciones de los nodos del grafo
        :param ANCHO: Configuración de la pantalla de pygame
        :param ALTO: Configuración de la pantalla de pygame
        :param C3: Coeficiente de movimiento
        '''
        for nodo in self.nodos:
            nodo.attr["X"] += C3 * nodo.attr["fuerza_x"]
            nodo.attr["Y"] += C3 * nodo.attr["fuerza_y"]
            nodo.attr["X"] = max(20, min(ANCHO - 20, nodo.attr["X"]))
            nodo.attr["Y"] = max(20, min(ALTO - 20, nodo.attr["Y"]))

    def recentrar_grafo(self, ANCHO, ALTO):
        '''
        Método para mantener el grafo centrado en la pantalla
        :param ANCHO: Configuración de la pantalla de pygame
        :param ALTO: Configuración de la pantalla de pygame
        '''
        # Calcular el centroide
        x_centro = sum(nodo.attr["X"] for nodo in self.nodos) / len(self.nodos)
        y_centro = sum(nodo.attr["Y"] for nodo in self.nodos) / len(self.nodos)
    
        # Coordenadas del centro de la pantalla
        centro_pantalla_x = ANCHO / 2
        centro_pantalla_y = ALTO / 2

        # Ajustar posiciones para centrar
        for nodo in self.nodos:
            nodo.attr["X"] += (centro_pantalla_x - x_centro)
            nodo.attr["Y"] += (centro_pantalla_y - y_centro)

    def limitar_a_margen(self, ANCHO, ALTO, margen=50):
        '''
        Método para obligar que el grafo no se pegue a los bordes de la pantalla
        :param ANCHO: Configuración de la pantalla de pygame
        :param ALTO: Configuración de la pantalla de pygame
        :param margen: Margen de la pantalla de pygame
        '''
        for nodo in self.nodos:
            nodo.attr["X"] = max(margen, min(ANCHO - margen, nodo.attr["X"]))
            nodo.attr["Y"] = max(margen, min(ALTO - margen, nodo.attr["Y"]))

    def agregar_fuerza_central(self, ANCHO, ALTO, fuerza_central=0.01):
        '''
        Agrega un coegiciente de fuerza central que obliga al grafo a mantenerse centrado
        :param ANCHO: Configuración de la pantalla de pygame
        :param ALTO: Configuración de la pantalla de pygame
        :param fuerza_central: Constante para mantener el grafo centrado
        '''
        centro_x = ANCHO / 2
        centro_y = ALTO / 2
        for nodo in self.nodos:
            dx = centro_x - nodo.attr["X"]
            dy = centro_y - nodo.attr["Y"]
            nodo.attr["fuerza_x"] += fuerza_central * dx
            nodo.attr["fuerza_y"] += fuerza_central * dy

    def dibujar(self, pantalla, BLANCO, NEGRO, AZUL):
        '''
        Dibuja el grafo en la patalla con pygame
        :param pantalla: pantalla de pygame
        :param BLANCO: Color a utilizar
        :param NEGRO: Color a utilizar
        :param AZUL: Color a utilizar
        '''
        pantalla.fill(BLANCO)
        for arco in self.aristas:
            pygame.draw.line(pantalla, NEGRO, (arco.nodoOrigen.attr["X"], arco.nodoOrigen.attr["Y"]),
                             (arco.nodoDestino.attr["X"], arco.nodoDestino.attr["Y"]), 2)
        for nodo in self.nodos:
            pygame.draw.circle(pantalla, AZUL, (int(nodo.attr["X"]), int(nodo.attr["Y"])), 10)
        pygame.display.flip()
        
    def SPRING(self, ANCHO, ALTO, BLANCO, NEGRO, AZUL, C1, C2, C3, ITERACIONES = 0):
        '''
        Algoritmo de P. Eades (1984) para distribuir los nodos de un grafo.
        :param ANCHO: Configuración de la pantalla de pygame
        :param ALTO: Configuración de la pantalla de pygame
        :param BLANCO: Color a utilizar
        :param NEGRO: Color a utilizar
        :param AZUL: Color a utilizar
        :param C1: constante de atracción
        :param C2: constante de repulsión
        :param C3: Coeficiente de movimiento
        :param ITERACIONES: Número máximo de iteraciones
        '''
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Visualización de grafos - Método Spring")
        reloj = pygame.time.Clock()
        # Configuración para el video
        FPS = 30
        NOMBRE_VIDEO = self.nombre + ".mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video = cv2.VideoWriter(NOMBRE_VIDEO, fourcc, FPS, (ANCHO, ALTO))
        
        for _ in range(ITERACIONES):
            self.calcular_fuerzas(C1, C2)
            self.agregar_fuerza_central(ANCHO, ALTO, fuerza_central=0.02)
            self.actualizar_posiciones(ANCHO, ALTO, C3)
            self.recentrar_grafo(ANCHO, ALTO)
            self.limitar_a_margen(ANCHO, ALTO)
            self.dibujar(pantalla, BLANCO, NEGRO, AZUL)
            # Convertir superficie de Pygame a un fotograma compatible con OpenCV
            frame = pygame.surfarray.array3d(pantalla)
            frame = np.transpose(frame, (1, 0, 2))  # Cambiar dimensiones a (altura, ancho, canales)
            video.write(frame)

            reloj.tick(FPS)
        
        pygame.image.save(pantalla, self.nombre + ".png")
        print("Captura guardada como: " + self.nombre + ".png")
        video.release
        pygame.quit()
        
    # MÉTODOS PROYECTO 6

    def calcular_repulsion_BH(self, quad_tree, nodo, theta=0.5):
        '''
        Calcula la fuerza de repulsión usando el algoritmo Barnes-Hut
        :param quad_tree: árbol cuádruple que contiene los nodos
        :param nodo: nodo para el cual calcular las fuerzas
        :param theta: parámetro de precisión (menor = más preciso)
        '''
        if not quad_tree.contiene_nodos:
            return 0, 0
        
        dx = quad_tree.centro_masa_x - nodo.attr["X"]
        dy = quad_tree.centro_masa_y - nodo.attr["Y"]
        dist = math.sqrt(dx * dx + dy * dy)
        
        # Si el nodo está en el mismo punto, evitar división por cero
        if dist < 0.0001:
            return 0, 0
        
        # Si el cluster está lo suficientemente lejos, tratar como una sola masa
        if quad_tree.ancho / dist < theta:
            f = quad_tree.total_masa / (dist * dist)
            return f * dx / dist, f * dy / dist
        
        # Si no, recursivamente calcular para cada cuadrante
        fx = fy = 0
        for hijo in quad_tree.hijos:
            if hijo:
                dfx, dfy = self.calcular_repulsion_BH(hijo, nodo, theta)
                fx += dfx
                fy += dfy
        
        return fx, fy

    def QuadTree(self, x, y, ancho, altura, nodos):
        '''
        Implementación de árbol cuádruple para Barnes-Hut
        :param x: coordenada x del cuadrante
        :param y: coordenada y del cuadrante
        :param ancho: ancho del cuadrante
        :param altura: altura del cuadrante
        :param nodos: lista de nodos en el cuadrante
        '''
        class Quad:
            def __init__(self, x, y, ancho, altura):
                self.x = x
                self.y = y
                self.ancho = ancho
                self.altura = altura
                self.hijos = [None] * 4
                self.centro_masa_x = 0
                self.centro_masa_y = 0
                self.total_masa = 0
                self.contiene_nodos = False
        
        quad = Quad(x, y, ancho, altura)
        
        if not nodos:
            return quad
        
        if len(nodos) == 1:
            quad.centro_masa_x = nodos[0].attr["X"]
            quad.centro_masa_y = nodos[0].attr["Y"]
            quad.total_masa = 1
            quad.contiene_nodos = True
            return quad
        
        # Dividir nodos en cuadrantes
        mid_x = x + ancho/2
        mid_y = y + altura/2
        cuadrantes = [[] for _ in range(4)]
        
        for nodo in nodos:
            idx = (int(nodo.attr["X"] > mid_x) << 1) | int(nodo.attr["Y"] > mid_y)
            cuadrantes[idx].append(nodo)
        
        # Recursivamente construir para cada cuadrante
        quad.hijos[0] = self.QuadTree(x, y, ancho/2, altura/2, cuadrantes[0])
        quad.hijos[1] = self.QuadTree(x, y + altura/2, ancho/2, altura/2, cuadrantes[1])
        quad.hijos[2] = self.QuadTree(x + ancho/2, y, ancho/2, altura/2, cuadrantes[2])
        quad.hijos[3] = self.QuadTree(x + ancho/2, y + altura/2, ancho/2, altura/2, cuadrantes[3])
        
        # Calcular centro de masa
        total_x = total_y = total_masa = 0
        for hijo in quad.hijos:
            if hijo and hijo.contiene_nodos:
                total_x += hijo.centro_masa_x * hijo.total_masa
                total_y += hijo.centro_masa_y * hijo.total_masa
                total_masa += hijo.total_masa
        
        if total_masa > 0:
            quad.centro_masa_x = total_x / total_masa
            quad.centro_masa_y = total_y / total_masa
            quad.total_masa = total_masa
            quad.contiene_nodos = True
        
        return quad

    def FruchtermanReingold(self, ANCHO, ALTO, BLANCO, NEGRO, AZUL, iteraciones=50, k=None, temp=1.0):
        '''
        Implementa el algoritmo de Fruchterman-Reingold para disposición de grafos
        :param ANCHO: Ancho de la ventana
        :param ALTO: Alto de la ventana
        :param BLANCO: Color de fondo
        :param NEGRO: Color de aristas
        :param AZUL: Color de nodos
        :param iteraciones: Número de iteraciones
        :param k: Distancia óptima entre nodos
        :param temp: Temperatura inicial para enfriamiento simulado
        '''
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Visualización de grafos - Fruchterman-Reingold")
        
        # Configuración para el video
        FPS = 30
        NOMBRE_VIDEO = self.nombre + "_FR.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video = cv2.VideoWriter(NOMBRE_VIDEO, fourcc, FPS, (ANCHO, ALTO))
        
        # Inicializar posiciones si no están definidas
        self.AsiganarValoresXY()
        
        # Calcular k si no se proporciona
        if k is None:
            area = ANCHO * ALTO
            k = math.sqrt(area / len(self.nodos))
        
        for i in range(iteraciones):
            # Inicializar fuerzas
            fuerzas = {nodo: [0, 0] for nodo in self.nodos}
            
            # Calcular fuerzas repulsivas
            for v in self.nodos:
                for u in self.nodos:
                    if v != u:
                        dx = v.attr["X"] - u.attr["X"]
                        dy = v.attr["Y"] - u.attr["Y"]
                        dist = math.sqrt(dx * dx + dy * dy)
                        if dist < 0.01: dist = 0.01
                        
                        # Fuerza repulsiva
                        f = k * k / dist
                        fx = f * dx / dist
                        fy = f * dy / dist
                        
                        fuerzas[v][0] += fx
                        fuerzas[v][1] += fy
            
            # Calcular fuerzas atractivas
            for arista in self.aristas:
                v = arista.nodoOrigen
                u = arista.nodoDestino
                dx = v.attr["X"] - u.attr["X"]
                dy = v.attr["Y"] - u.attr["Y"]
                dist = math.sqrt(dx * dx + dy * dy)
                if dist < 0.01: dist = 0.01
                
                # Fuerza atractiva
                f = dist * dist / k
                fx = f * dx / dist
                fy = f * dy / dist
                
                fuerzas[v][0] -= fx
                fuerzas[v][1] -= fy
                fuerzas[u][0] += fx
                fuerzas[u][1] += fy
            
            # Aplicar fuerzas con límite de temperatura
            t = temp * (1 - i/iteraciones)
            for v in self.nodos:
                fx = min(max(fuerzas[v][0], -t), t)
                fy = min(max(fuerzas[v][1], -t), t)
                v.attr["X"] += fx
                v.attr["Y"] += fy
                
                # Mantener dentro de los límites
                v.attr["X"] = min(ANCHO-10, max(10, v.attr["X"]))
                v.attr["Y"] = min(ALTO-10, max(10, v.attr["Y"]))
            
            # Dibujar el estado actual
            self.dibujar(pantalla, BLANCO, NEGRO, AZUL)
            
            # Guardar frame
            frame = pygame.surfarray.array3d(pantalla)
            frame = np.transpose(frame, (1, 0, 2))
            video.write(frame)
        
        pygame.image.save(pantalla, self.nombre + "_FR.png")
        print(f"Visualización Fruchterman-Reingold guardada como: {self.nombre}_FR.png")
        video.release()
        pygame.quit()

    def BarnesHut(self, ANCHO, ALTO, BLANCO, NEGRO, AZUL, iteraciones=50, theta=0.5, temp=1.0):
        '''
        Implementa el algoritmo Barnes-Hut para disposición de grafos
        :param ANCHO: Ancho de la ventana
        :param ALTO: Alto de la ventana
        :param BLANCO: Color de fondo
        :param NEGRO: Color de aristas
        :param AZUL: Color de nodos
        :param iteraciones: Número de iteraciones
        :param theta: Parámetro de precisión Barnes-Hut
        :param temp: Temperatura inicial para enfriamiento simulado
        '''
        pygame.init()
        pantalla = pygame.display.set_mode((ANCHO, ALTO))
        pygame.display.set_caption("Visualización de grafos - Barnes-Hut")
        
        # Configuración para el video
        FPS = 30
        NOMBRE_VIDEO = self.nombre + "_BH.mp4"
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        video = cv2.VideoWriter(NOMBRE_VIDEO, fourcc, FPS, (ANCHO, ALTO))
        
        # Inicializar posiciones si no están definidas
        self.AsiganarValoresXY()
        
        for i in range(iteraciones):
            # Construir QuadTree
            quad_tree = self.QuadTree(0, 0, ANCHO, ALTO, self.nodos)
            
            # Calcular fuerzas para cada nodo
            fuerzas = {nodo: [0, 0] for nodo in self.nodos}
            
            for v in self.nodos:
                # Calcular fuerzas repulsivas usando Barnes-Hut
                fx, fy = self.calcular_repulsion_BH(quad_tree, v, theta)
                fuerzas[v][0] += fx
                fuerzas[v][1] += fy
                
                # Calcular fuerzas atractivas (solo para nodos conectados)
                for arista in v.listaAdyacencia:
                    u = arista.nodoDestino
                    dx = v.attr["X"] - u.attr["X"]
                    dy = v.attr["Y"] - u.attr["Y"]
                    dist = math.sqrt(dx * dx + dy * dy)
                    if dist < 0.01: dist = 0.01
                    
                    # Fuerza atractiva
                    f = dist / 100  # Factor de atracción
                    fx = f * dx / dist
                    fy = f * dy / dist
                    
                    fuerzas[v][0] -= fx
                    fuerzas[v][1] -= fy
            
            # Aplicar fuerzas con límite de temperatura
            t = temp * (1 - i/iteraciones)
            for v in self.nodos:
                fx = min(max(fuerzas[v][0], -t), t)
                fy = min(max(fuerzas[v][1], -t), t)
                v.attr["X"] += fx
                v.attr["Y"] += fy
                
                # Mantener dentro de los límites
                v.attr["X"] = min(ANCHO-10, max(10, v.attr["X"]))
                v.attr["Y"] = min(ALTO-10, max(10, v.attr["Y"]))
            
            # Dibujar el estado actual
            self.dibujar(pantalla, BLANCO, NEGRO, AZUL)
            
            # Guardar frame
            frame = pygame.surfarray.array3d(pantalla)
            frame = np.transpose(frame, (1, 0, 2))
            video.write(frame)
        
        pygame.image.save(pantalla, self.nombre + "_BH.png")
        print(f"Visualización Barnes-Hut guardada como: {self.nombre}_BH.png")
        video.release()
        pygame.quit()