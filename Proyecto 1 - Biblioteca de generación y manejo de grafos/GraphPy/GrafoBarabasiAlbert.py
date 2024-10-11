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
    grafo = Grafo("Bara " + str(n) + "-nodos " + dirstr, dir = dirigido, geo = True)
    
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
    
    tam = d # Tamaño actual de la lista de nodos    
    while i < n:
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
        tam = tam + 1
        j = 0
        while j < d:
            numero_aleatorio = random.randrange(0, tam)
            nodoDestino = grafo.nodos[numero_aleatorio]
            if(isinstance(nodoDestino, Nodo) and numero_aleatorio != i and nodo != nodoDestino):
                if(nodoDestino.deg() < d):
                    #print("Si")
                    volada = random.random()
                    v = nodoDestino.deg()
                    p = 1 - v/d
                    if(volada < p):
                        arco1 = Arista(nodo, nodoDestino)
                        arco2 = Arista(nodoDestino, nodo)
                        print(grafo.ExisteArco(arco1) == False)
                        print()
                        if(dirigido == True):
                            nodo.listaAdyacencia.append(arco1)
                            j = j + 1
                        elif(dirigido == False):
                            nodo.listaAdyacencia.append(arco1)
                            nodo.listaAdyacencia.append(arco2)
                            j = j + 1
        i = i + 1
    
            
    return grafo
                
