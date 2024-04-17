from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        
        
        curr = frontier.pop() #Curr - > current node we will operate on

        for node in graph[curr]: #We look at the node's neighbors

            if node not in result: #If we haven't already seen the node...
                result.add(node) #We add it to the seen list
                frontier.add(node) #And to the frontier
    

    return result





def connected(graph):
    
    start = next(iter(graph)) #Start from arbitrary node
    reachednode = reachable(graph, start) 

    return (len(reachednode)) == len(graph) #If the length of the graph is not the reached area, its not connected




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    
    visited = set() #We need to keep track of visited nodes
    count = 0 #Counts components

    #This function is basically a combination of reachable and connected
    #As far as the logic goes
    for node in graph:

        if node not in visited:

            n_reachable = reachable(graph, node)
            visited.update(n_reachable)
            count += 1
    
    return count
