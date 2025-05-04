import graph
import math
import sys
import queue
import dijkstra

def SalesmanTrackBacktracking(g,visits):
    track = graph.Track(g) 
    
    start = visits.Vertices[0]
    end = visits.Vertices[-1]
    list_nodes = []
    #min_dist = sys.float_info.max
    
    sol = [[], sys.float_info.max]
    
    RecBacktracking(sol, start, [], list_nodes, end, 0, visits)
    track.Edges.extend(sol[0])
    return track
    
def RecBacktracking(solution, vertex_actual, path_actual, list_nodes, end, dist_actual, visits):
    #n = vertex_actual.Name
    list_nodes.append(vertex_actual)
    
    if dist_actual >= solution[-1]: #Cami actual més gran que solució anterior
        list_nodes.pop()
        return  
    
    tots = True
    for v in visits.Vertices: 
        if v not in list_nodes: 
            tots = False
    
    if vertex_actual == visits.Vertices[-1] and tots == True: #Solució
        solution = list(path_actual)
        list_nodes.pop()
        return solution, dist_actual
    
    vertex_next = None
    for edge in vertex_actual.Edges: 
        if edge.Saved == False: 
            edge.Saved = True
            vertex_next = edge.Destination
            #e = edge.Name
            #v = vertex_next.Name
            path_actual.append(edge)
            
            sol = RecBacktracking(solution, vertex_next, path_actual, list_nodes, end, dist_actual+edge.Length, visits)
            
            if sol is not None:     
                solution[0] = sol[0]
                solution[-1] = sol[-1]
            
            path_actual.pop()
            edge.Saved = False
            
    list_nodes.pop()    
    return 

# ==============================================================================

def SalesmanTrackBacktrackingGreedy(g, visits):
    return graph.Track(g)

