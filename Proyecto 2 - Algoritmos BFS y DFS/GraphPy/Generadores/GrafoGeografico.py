from ..Estructura.Nodo import Nodo
from ..Estructura.Grafo import Grafo
from ..Estructura.Arista import Arista
import math

def grafoGeografico(n, r, dirigido=False):
    """
    Genera grafo aleatorio con el modelo geográfico simple
    :param n: número de nodos (> 0)
    :param r: distancia máxima para crear un nodo (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("Geo " + str(n) + "-nodos " + dirstr, dir = dirigido, geo = True)
    
    for i in range(n):
        nodo = Nodo("N-" + str(i), geo = True)
        grafo.AgregarNodo(nodo)
        
    for nodo in grafo.nodos:
        i = 1
        while i < n:
            nodoDestino = grafo.nodos[i]
            if(isinstance(nodo, Nodo) and isinstance(nodoDestino, Nodo) and nodo != nodoDestino):
                dist = math.dist([nodo.X, nodo.Y], [nodoDestino.X, nodoDestino.Y])
                if(dist <= r):
                    arco1 = Arista(nodo, nodoDestino)
                    arco2 = Arista(nodoDestino, nodo)
                    if(dirigido == True and grafo.ExisteArco(arco1) == False):
                        nodo.listaAdyacencia.append(arco1)
                    elif(dirigido == False and grafo.ExisteArco(arco1) == False and grafo.ExisteArco(arco2) == False):
                        nodo.listaAdyacencia.append(arco1)
            i = i + 1
    
    return grafo
    