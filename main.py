#!/bin/python3

import math
import os
import random
import re
import sys

'''
#given n is the dimension of a nxn squared chess board
#given knight starting position
#given bishop stationary position
#given destination coordinate
#compute, shortest route from starting to destination for the knight using legal moves
#make sure to evade the tiles that the bishop could threaten from its stationery position

General Approach:
model as graph, with vertices as valid tiles for the knight, edges meaning a valid route
take out coordinates that are threatened by bishop
run Dijsktraß
'''




#
# Complete the 'moves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER startRow
#  3. INTEGER startCol
#  4. INTEGER endRow
#  5. INTEGER endCol
#  6. INTEGER bishopRow
#  7. INTEGER bishopCol
#





global graph1
graph1 = {}
global nodedict
nodedict = {}

def moves(n, startRow, startCol, endRow, endCol, bishopRow, bishopCol):
    # Write your code here
    start = (startRow, startCol)
    end = (endRow, endCol)
    
    graph1 = makeGraph(n)
    bishopthreat = addBishop(bishopRow, bishopCol, n)
    populateGraph(n,graph1, bishopthreat, start)
    dijkstra(graph1, start)
    

    return nodedict[end].d
    
def makeGraph(n):
    global graph1
    
    global nodedict
    

    for i in range(n):
        x = i
        for j in range(n):
            q = Node((x,j))
            graph1[q] = []
            nodedict[(x,j)] = q

    
    return graph1

    #populate graph for each vertex = tile, map possible knight moves, as adj list

def addBishop(bishopRow, bishopCol, n):
    
    bishopthreat = []
    
    for i in range(n):
        new_row = bishopRow + 1
        new_column = bishopCol + 1
        
        if new_row < n and new_column < n:
            bishopthreat.append((new_row, new_column)) 
    
    for i in range(n, 0, -1):
        new_row = bishopRow -1
        new_column = bishopCol - 1
        
        if new_row < n and new_column < n:
            bishopthreat.append((new_row, new_column)) 
    
    return bishopthreat

class Node:
    def __init__(self, node):
        self.d = 100000000
        self.id = node
        self.parent = None
    
def populateGraph(n, graph1, bishopthreat, start):
    
    global nodedict
    
    #possible moves of knight
    xmove = [2, 1, -1, -2, -2, -1, 1, 2]
    ymove = [1, 2, 2, 1, -1, -2, -2, -1]
    
    for each in graph1:
        for i in range(8):
          x = each.id[0] + xmove[i]
          y = each.id[1] + ymove[i]
            
          if (x,y) in bishopthreat:
            continue
          elif x < 0 or y <0:
            continue
          elif x > n-1 or y > n-1:
            continue
          else:
            newNode = nodedict[(x,y)]
            graph1[each].append(newNode)
    
    return graph1


def relax(u, v):
    if v.d > u.d + 1:
        v.d = u.d + 1
        v.parent = u

def dijkstra(graph1, start):
    #set start as root of dijkstra
    global nodedict
    nodedict[start].d = 0
    
    
    Q = []
    S = []
    
    for each in nodedict:
        Q.append(nodedict[each])
    
    while Q != []:
        Q.sort(key=lambda x: x.d, reverse=False)
        u = Q.pop(0)
        for each in graph1[u]:
            relax(u, each)
        

q = moves(6, 1, 2, 4, 5, 6, 7)
print(q)