from typing import Any
import networkx as nx
from matplotlib import pyplot as plt

def dfs(g: nx.Graph, start_node: Any) -> list:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    print(g, start_node)
    return list(g.nodes)

if __name__ == '__main__':

    a = [
        'A B C',
        'B A D',
        'C A D',
        'D B C E',
        'E D'
    ]

    g = nx.parse_adjlist(a)
    nx.draw(g, with_labels=True)
    plt.show()


    vertax = [-1]*len(g)

    list_vertax = []
    start_elem= 0
    while start_elem < len(list_vertax):
        u = list_vertax[start_elem]
        start_elem +=1
        for v in list_vertax[u]:
            if vertax[v] is None:
                vertax[v] = vertax[u] + 1
                list_vertax.append(v)
        print(list_vertax)




