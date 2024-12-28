def G_Vertices(Graph):
    Gate = 0
    if type(Graph) != list:
        Gate = 1
    else:
        for i in Graph:
            if type(i) != list:
                Gate = 1
                break
            elif len(i) != 2:
                Gate = 1
                break
            elif type(i[0]) != set or type(i[1]) not in {int , float}:
                Gate = 1
                break
            elif len(i[0]) != 2:
                Gate = 1
                break

    if Gate == 1:
        return "Input Error"
    if Gate == 0:
        U = set()
        for i in Graph:
            U = set.union(U , i[0])

    return U

def Path1(Initial_Vertex , Graph):
    if G_Vertices(Graph) == "Input Error":
        return "Graph Input Error"
    else:
        if Initial_Vertex not in G_Vertices(Graph):
            return "Vertex Input Error"
        else:
            Edges = []
            for i in Graph:
                if Initial_Vertex in i[0]:
                    for vertex in G_Vertices(Graph):
                        if vertex != Initial_Vertex and vertex in i[0]:
                            Edges.append([Initial_Vertex , vertex])

    return Edges


def path2(Initial_Vertex , Graph):
    if G_Vertices(Graph) == "Input Error":
        return "Graph Input Error"
    else:
        if Initial_Vertex not in G_Vertices(Graph):
            return "Vertex Input Error"
        else:
            Edges = []
            for i in Path1(Initial_Vertex , Graph):
                for j in G_Vertices(Graph):
                    if j != i[0] and j != i[1] and [i[1] , j] in Path1(i[1] , Graph):
                        Edges.append([i[0] , i[1] , j])

    if Edges == []:
        return "There is no path with two edges starting the initial vertex"
    else:
        return Edges
                       