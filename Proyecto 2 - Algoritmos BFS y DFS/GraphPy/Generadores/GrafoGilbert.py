from ..Estructura.Nodo import Nodo
from ..Estructura.Arista import Arista
from ..Estructura.Grafo import Grafo
import random

def grafoGilbert(n, p, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Gilbert
    :param n: número de nodos (> 0)
    :param p: probabilidad de crear una arista (0, 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("Gilbert " + str(n) + "," + str(p) + dirstr, dir = dirigido)
    
    for i in range(n):
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
        
    for nodo in grafo.nodos:
        i = 0
        if(isinstance(nodo, Nodo)):
            while i < n:
                numero_aleatorio2 = random.randrange(0, n)
                volada = random.random()
                nodoDestino = grafo.nodos[numero_aleatorio2]
                if(isinstance(nodoDestino, Nodo) and nodo != nodoDestino and volada <= p):
                    arco1 = Arista(nodo, nodoDestino)
                    arco2 = Arista(nodoDestino, nodo)
                    if(dirigido == True and grafo.ExisteArco(arco1) == False):
                        nodo.listaAdyacencia.append(arco1)
                    elif(dirigido == False and grafo.ExisteArco(arco1) == False and grafo.ExisteArco(arco2) == False):
                        nodo.listaAdyacencia.append(arco1)
                i = i + 1
    return grafo