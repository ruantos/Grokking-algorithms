""" Implementing breadth-first search algorithm"""
from collections import deque

def is_seller(person):
    """ Checks if a name ends with m"""
    return "salesman" in person

def breadth_first(graph, name):
    """ Searching for a seller in your personal network"""
    search = deque()
    search += grafo[name]
    searched = []
    while search:
        person = search.popleft()
        if person not in searched:
            if is_seller(person):
                print(person + " Is a seller!")
                return True
            else:
                search += graph[person]
                searched.append(person)
    print("There is no salesman")
    return False


grafo = {}
grafo["you"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom salesman", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

breadth_first(grafo, "you")
