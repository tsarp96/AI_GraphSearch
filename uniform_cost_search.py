# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import numpy as np
import sys

def getInput(path):
    maze = []
    with open(path) as f:
        content = f.readlines()
        for idx, line in enumerate(content):
            line = line.strip()
            maze.append([])
            for square in line.split(','):
                maze[idx].append(square)
    return maze

maze = getInput('maze_format.txt')

def setInitialState():
    for i in range(len(maze)):
        for k in range(len(maze[0])):
            if 'S' in maze[i][k]:
                return i,k
            
def whereCanIGo(i,k):
    possible_moves = [1,1,1,1,0]
    #[right,down,left,up,stop]
    if 'l' in maze[i][k]:
        possible_moves[2] = 0
    if 'r' in maze[i][k]:
        possible_moves[0] = 0
    if 'u' in maze[i][k]:
        possible_moves[3] = 0
    if 'd' in maze[i][k]:
        possible_moves[1] = 0
    if 'G' in maze[i][k]:
        possible_moves[4] = 1
    return possible_moves

def goRight(i,k):
    k=k+1
    return i,k
def goLeft(i,k):
    k=k-1
    return i,k
def goDown(i,k):
    i=i+1
    return i,k
def goUp(i,k):
    i=i-1
    return i,k

def goalTest(state):
    if 'G' in maze[state[0]][state[1]]:
        return True
    else:
        return False
    
def getMoves(i,k,possible_moves):
    #[left,right,up,down,stop]
    moves = []
    if possible_moves[0] == 1:
        moves.append(goRight(i,k))
    if possible_moves[1] == 1:
        moves.append(goDown(i,k))
    if possible_moves[2] == 1:
        moves.append(goLeft(i,k))
    if possible_moves[3] == 1:
        moves.append(goUp(i,k))
    
    return moves

def calc_path_cost(move):
    if 'T' in maze[move[0]][move[1]]:
        return 7
    else:
        return 1

def getLowestCostIndex(frontier):
    path_costs = []
    for node in frontier:
        path_costs.append(node.pathCost)
    min_val = min(path_costs)
    return path_costs.index(min_val)
 
class Node():
    state = None
    pathCost = 0
    parent = None
    child = None
    depth = None

def UniformCostSearch():
    explored = []
    frontier = []
    node = Node()
    node.state = []
    node.depth = 0
    initialState = setInitialState()
    node.state = initialState
    if goalTest(node.state) == True:
        print('solution')
        print(node.state)
        return sys.exit(1)
    frontier.append(node)
    for i in range(100000):
        if len(frontier) == 0:
            return 'failure'
            break
        
        
       
        
        index = getLowestCostIndex(frontier)
        current_node = frontier.pop(index)
        
        frontier_ = []
        for node in frontier:
            frontier_.append(node.state)
        print("Last Frontier")
        print(frontier_)
        
        #print(current_node.pathCost)
        
        explored.append(current_node)
        
        explored_ = []
        for node in explored:
            explored_.append(node.state)
        print("Explored")
        print(explored_)
        
        moves = getMoves(current_node.state[0],current_node.state[1],whereCanIGo(current_node.state[0],current_node.state[1]))
       
        
        
        for move in moves:
            child = Node()
            current_node.child = child
            child.parent = current_node
            child.pathCost =  calc_path_cost(move) + current_node.pathCost
            child.state = move
            if child.state not in explored_ or frontier_:
                if goalTest(child.state) == True:
                    total_path_cost = child.pathCost
                    print('solution :')
                    print(child.state)
                    goal_path = []
                    goal_path.append(child.state)
                    while child.parent != None:
                        child = child.parent
                        goal_path.append(child.state)
                        #print(child.pathCost)
                    print("Goal Path : ")
                    print(goal_path)
                    print("Total Path Cost : %d " % total_path_cost)
                    
                    return sys.exit(1)
            if child.state not in explored_:
                frontier.append(child)
        
                
        

UniformCostSearch()






     
    

    
    