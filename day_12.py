from input_reader import read
import re
import networkx as nx

input_lines = read.inputLines(12)

def parseInput(input):
    return [re.findall(r"(\w+)-(\w+)", line)[0] for line in input]

DATA = parseInput(input_lines)
print(DATA)

#============================= Part One =============================

graph = nx.Graph()
graph.add_edges_from(DATA)
paths = []

def possPath(graph, start, currentPath):
    adj = list(graph.neighbors(start))

    for node in adj:
        if (node == 'end'):
            paths.append(currentPath + ['end'])
        elif not (node.islower() and node in currentPath):
            possPath(graph, node, currentPath + [node])

possPath(graph, 'start', ['start'])
print(len(paths))

#============================= Part Two =============================

paths = []

def isEligible(cave, currentPath):
    if cave == 'start':
        return False
    if (cave == 'end' and currentPath.count('end') == 0) or (not cave.islower()):
        return True
    
    if (cave in currentPath):
        for cav in currentPath:
            if currentPath.count(cav) > 1 and cav.islower():
                return False
    
    return True

def possPath2(graph, start, currentPath):
    adj = list(graph.neighbors(start))

    for node in adj:
        if (node == 'end'):
            paths.append(currentPath + ['end'])
        elif isEligible(node, currentPath):
            possPath2(graph, node, currentPath + [node])

possPath2(graph, 'start', ['start'])
print(len(paths))