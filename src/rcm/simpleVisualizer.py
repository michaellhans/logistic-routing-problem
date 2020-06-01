# visualizer.py
# Module to visualize the map and the streets in simple way

import graphviz

# Check if the street is in route
def CheckStreetInRoute(origin, destination, route):
    for i in range (len(route)-1):
        if ((route[i] == int(origin)) and (route[i+1] == int(destination))):
            return True
    return False

# Visualize the graph from street, route, and length of the map information
def VisualizeGraph(streets, route, length, fileNode):
    dot = graphviz.Graph(comment='Sthyrelest City')
    for city in route:
        dot.node(str(city), style='filled', color='black', fillcolor='yellow')

    for street in streets:
        if ((CheckStreetInRoute(street[1], street[2], route)) or (CheckStreetInRoute(street[2], street[1], route))):
            dot.edge(street[1], street[2], constraint='true', label=street[3], color='red')
        else:
            dot.edge(street[1], street[2], constraint='true', label=street[3])
            
    dot.render('../bin/'+fileNode, view=True)