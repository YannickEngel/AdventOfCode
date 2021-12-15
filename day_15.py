from input_reader import read
import re
import numpy as np
import networkx as nx
import time

input_lines = read.inputLines(15)

def parseInput(input):
    temp = []
    for line in input:
        temp.append([int(val) for val in re.findall(r"(\d)", line)])
    return temp

DATA = np.matrix(parseInput(input_lines))
#============================= Part One =============================

def generateGraph(data):
    G = nx.DiGraph()
    y,x = data.shape
    for i in range(y):
        for j in range(x):
            G.add_node((i, j))
            for dy, dx in (0,1),(1,0),(0,-1),(-1,0):
                if( 0 <= i+dy <y and 0 <= j+dx <x):
                    G.add_edge((i, j), (i+dy, j+dx), weight = data[i+dy,j+dx])
    return G

beg = time.time()
G1 = generateGraph(DATA)
print(f"Result Part 1: {nx.shortest_path_length(G1, (0,0), (DATA.shape[0] - 1 , DATA.shape[1] - 1), weight='weight')} \t {(time.time() -beg)*1000} ms")


#============================= Part Two =============================

beg = time.time()
newArr = np.zeros((DATA.shape[0] * 5, DATA.shape[1] * 5))
y,x = DATA.shape

for i in range(5):
    for j in range(5):
        temp = DATA
        for k in range(i+j):
            temp = temp +1
            temp[temp > 9] = 1
        newArr[i*y: (i+1)*y, j*x:(j+1)*x] = temp


G2 = generateGraph(newArr)
print(f"Result Part 2: {nx.shortest_path_length(G2, (0,0), (newArr.shape[0] - 1 , newArr.shape[1] - 1), weight='weight')} \t {(time.time() -beg)*1000} ms")
