from ..Estructura.Nodo import Nodo
from ..Estructura.Arista import Arista
from ..Estructura.Grafo import Grafo

def grafoMalla(m, n, dirigido=False):
    """
    Genera grafo de malla
    :param m: número de columnas (> 1)
    :param n: número de filas (> 1)
    :param dirigido: el grafo es dirigido?
    :return: grafo generado
    """
    dirstr = "NoDir"
    if(dirigido == True): dirstr = "Dir"
    grafo = Grafo("grafoMalla " + str(m) + "x" + str(n) + " " + dirstr, dir = dirigido)
  
    mXnNodos = []
    
    for i in range(m):
        Nodos = []
        for j in range(n):
            cnodo = Nodo("N"+ str(i) + "," + str(j))
            Nodos.append(cnodo)
            grafo.AgregarNodo(cnodo)
            
        mXnNodos.append(Nodos)
        
    for i in range(m):
        for j in range(n):
            if((i + 1) < m):
              nnode = mXnNodos[i+1][j]
              cnode = mXnNodos[i][j]
              if(isinstance(cnode, Nodo) and isinstance(nnode, Nodo)):
                  cnode.listaAdyacencia.append(Arista(cnode, nnode))
            if((j + 1) < n):
              nnode = mXnNodos[i][j+1]
              cnode = mXnNodos[i][j]
              if(isinstance(cnode, Nodo) and isinstance(nnode, Nodo)):
                  cnode.listaAdyacencia.append(Arista(cnode, nnode))
            
        
    return grafo