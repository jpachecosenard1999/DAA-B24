from GraphPy.GrafoMalla import grafoMalla
from GraphPy.GrafoErdosRenyi import grafoErdosRenyi
from GraphPy.GrafoGilbert import grafoGilbert
from GraphPy.GrafoGeografico import grafoGeografico
from GraphPy.GrafoBarabasiAlbert import grafoBarabasiAlbert

# grafo = grafoMalla(3,3)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoMalla(3,3, dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoErdosRenyi(15,30,dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoErdosRenyi(15,30)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoGilbert(15, .4)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoGilbert(15, .4, dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoGeografico(15, .4)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoGeografico(15, .4, dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

grafo = grafoBarabasiAlbert(15, 4)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoBarabasiAlbert(15, 4, dirigido = True)

grafo.MostrarGrafo()

grafo.Guardar()