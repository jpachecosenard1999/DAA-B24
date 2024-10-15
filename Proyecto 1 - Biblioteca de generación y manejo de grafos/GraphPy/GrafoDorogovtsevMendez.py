from .Arista import Arista
from .Nodo import Nodo
from .Grafo import Grafo
import random

def grafoDorogovtsevMendes(n, dirigido=False):
    """
    Genera grafo aleatorio con el modelo Barabasi-Albert
    :param n: número de nodos (≥ 3)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("Doro " + str(n) + "-nodos " + dirstr, dir = dirigido, geo = False)
    
    for i in range(n):
        nodo = Nodo("N-" + str(i))
        grafo.AgregarNodo(nodo)
        
    # Conectar los 3 primeros para formar un triángulo
    for i in range(3):
        for j in range(3):
            nodoOrigen = grafo.nodos[i]
            nodoDestino = grafo.nodos[j]
            if(nodoOrigen != nodoDestino and isinstance(nodoOrigen, Nodo) and isinstance(nodoDestino, Nodo)):
                arco1 = Arista(nodoOrigen, nodoDestino)
                arco2 = Arista(nodoDestino, nodoOrigen)
                if(dirigido == True and grafo.ExisteArco(arco1) == False):
                    grafo.AgregarArco(arco1)
                elif(dirigido == False and grafo.ExisteArco(arco1) == False and grafo.ExisteArco(arco2) == False):
                    grafo.AgregarArco(arco1)
                    grafo.AgregarArco(arco2)
    for i in range(3, n):
        nodoOrigen = grafo.nodos[i]
        naristas = len(grafo.aristas)
        numero_aleatorio = random.randrange(0,naristas)
        arista = grafo.aristas[numero_aleatorio]
        if(isinstance(arista, Arista) and isinstance(nodoOrigen, Nodo)):
            nodoa = arista.nodoOrigen
            nodob = arista.nodoDestino
            extremos = [nodoa, nodob]
            for e in extremos:
                arco1 = Arista(nodoOrigen, e)
                arco2 = Arista(e, nodoOrigen)
                if(dirigido == True and grafo.ExisteArco(arco1) == False):
                    grafo.AgregarArco(arco1)
                elif(dirigido == False and grafo.ExisteArco(arco1) == False and grafo.ExisteArco(arco2) == False):
                    grafo.AgregarArco(arco1)
                    grafo.AgregarArco(arco2)
                    
    return grafo
                
    
    
                    
    
                    
    