from graphviz import Digraph

# Create a new Digraph
dot = Digraph()

# Add nodes
dot.node('A', 'Google Cloud Platform')
dot.node('B', 'Compute Engine')
dot.node('C', 'Cloud Storage')

# Add edges
dot.edges(['AB', 'AC'])

# Render the graph
dot.render('gcp_architecture', format='png', cleanup=True)
