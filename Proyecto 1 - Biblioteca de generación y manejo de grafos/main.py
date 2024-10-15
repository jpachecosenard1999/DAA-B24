from GraphPy.GrafoMalla import grafoMalla
from GraphPy.GrafoErdosRenyi import grafoErdosRenyi
from GraphPy.GrafoGilbert import grafoGilbert
from GraphPy.GrafoGeografico import grafoGeografico
from GraphPy.GrafoBarabasiAlbert import grafoBarabasiAlbert
from GraphPy.GrafoDorogovtsevMendez import grafoDorogovtsevMendes

# grafo = grafoMalla(50, 10)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoMalla(50, 10, dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoErdosRenyi(500,1000,dirigido = True)

# grafo.MostrarGrafo()

# grafo.Guardar()

# grafo = grafoErdosRenyi(500,1000)

# grafo.MostrarGrafo()

# grafo.Guardar()

grafo = grafoGilbert(500, .4)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoGilbert(500, .4, dirigido = True)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoGeografico(500, .4)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoGeografico(500, .4, dirigido = True)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoBarabasiAlbert(500, 4)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoBarabasiAlbert(500, 4, dirigido = True)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoDorogovtsevMendes(500)

grafo.MostrarGrafo()

grafo.Guardar()

grafo = grafoDorogovtsevMendes(500, dirigido = True)

grafo.MostrarGrafo()

grafo.Guardar()