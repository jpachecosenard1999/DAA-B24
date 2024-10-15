from .Nodo import Nodo
from .Grafo import Grafo
from .Arista import Arista
import random

def grafoBarabasiAlbert(n, d, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (> 0)
    :param d: grado máximo esperado por cada nodo (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("Bara " + str(n) + "-nodos " + dirstr, dir = dirigido, geo = False)
    
    for i in range(d):
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
        
    # Conecto los primeros d nodos
    
    for i in range(d):
        for j in range(d):
            nodoOrigen = grafo.nodos[i]
            nodoDestino = grafo.nodos[j]
            if(i != j and isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo)):
                arco1 = Arista(nodoOrigen, nodoDestino)
                arco2 = Arista(nodoDestino, nodoOrigen)
                if(dirigido == True and grafo.ExisteArco(arco1) == False):
                    nodoOrigen.listaAdyacencia.append(arco1)
                elif(dirigido == False and grafo.ExisteArco(arco1) == False and grafo.ExisteArco(arco2) == False):
                    nodoOrigen.listaAdyacencia.append(arco1)
                    nodoDestino.listaAdyacencia.append(arco2)
                    
    i = d - 1 # Ya están creados los d primeros nodos (0, 1, 2, ..., d-1)
    while i < n:
        baraja = grafo.nodos.copy()
        random.shuffle(baraja)
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
        for b in baraja:
            nodoDestino = b
            if(isinstance(nodoDestino, Nodo) and nodo != nodoDestino):
                if(nodoDestino.deg() < d):
                    volada = random.random()
                    v = nodoDestino.deg()
                    p = 1 - v/d
                    if(volada < p):
                        arco1 = Arista(nodo, nodoDestino)
                        arco2 = Arista(nodoDestino, nodo)
                        if(dirigido == True):
                            nodo.listaAdyacencia.append(arco1)
                        elif(dirigido == False):
                            nodo.listaAdyacencia.append(arco1)
                            nodoDestino.listaAdyacencia.append(arco2)
        i = i + 1
    
            
    return grafo
                
