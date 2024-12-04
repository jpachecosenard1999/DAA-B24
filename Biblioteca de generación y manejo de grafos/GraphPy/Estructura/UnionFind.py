class UnionFind:
    def __init__(self, nodes):
        '''
        Clase auxiliar para manejar uniones entre conjuntos disjuntos
        '''
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        '''
        Método recursivo para encontrar el camino de un nodo
        :param: nodo a encontrar camino
        :return: ancestro del nodo
        '''
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        '''
        Clase para unir dos conjuntos
        :param: nodo origen
        :param: nodo destino
        '''
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1