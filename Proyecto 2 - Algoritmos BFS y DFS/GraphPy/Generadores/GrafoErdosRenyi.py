from ..Estructura.Nodo import Nodo
from ..Estructura.Arista import Arista
from ..Estructura.Grafo import Grafo
import random

def grafoErdosRenyi(n, m, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Erdos-Renyi
    :param n: número de nodos (> 0)
    :param m: número de aristas (>= n-1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("ErdosRenyi " + str(n) + "-nodos " + dirstr, dir = dirigido)
    
    for i in range(n):
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
          
    aristas = 0
    
    while aristas < m:
        numero_aleatorio1 = random.randrange(0, n)
        numero_aleatorio2 = random.randrange(0, n)
        if(numero_aleatorio1 != numero_aleatorio2):
            nodoOrigen = grafo.nodos[numero_aleatorio1]
            nodoDestino = grafo.nodos[numero_aleatorio2]
            if(isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo)):
                if(dirigido == True):
                    arco = Arista(nodoOrigen, nodoDestino)
                    if(grafo.ExisteArco(arco) == False):
                        nodoOrigen.listaAdyacencia.append(arco)
                        aristas = aristas + 1
                elif(dirigido == False):
                    arco = Arista(nodoOrigen, nodoDestino)
                    arco2 = Arista(nodoDestino, nodoOrigen)
                    if(grafo.ExisteArco(arco) == False and grafo.ExisteArco(arco2) == False):
                        nodoOrigen.listaAdyacencia.append(arco)
                        aristas = aristas + 1
    return grafo
                        