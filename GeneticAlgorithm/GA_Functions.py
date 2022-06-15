import numpy as np
from copy import deepcopy
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from Greedy.greedy_function import GreedySolution

"""
We have total of 48 nodes in a route
constGenes: Out of which we will take 20-30 nodes from one parent (this number is chosen randomly)
constGenesLoc: Starting point of these constent genes is also selected randomly
rest from other parent
"""


def OrderCrossover(route1,route2):
    constGenes = np.random.randint(0,47)
    constGenesLoc = np.random.randint(0,len(route1.path)-constGenes)
    #print("st Loc, len ",constGenesLoc,constGenes)
    parent1 = route1.path
    parent2 = route2.path

    parent1Copy = deepcopy(parent1)
    parent2Copy = deepcopy(parent2)

    child1 = [None for i in range(len(parent1))]
    child2 = [None for i in range(len(parent2))]

    #child1[0:constGenes] = parent1Copy[constGenesLoc:constGenesLoc+constGenes]
    child1[constGenesLoc:constGenesLoc + constGenes] = parent1Copy[constGenesLoc:constGenesLoc + constGenes]
    parent1ReducedIndex = [city.index for city in parent1[:constGenesLoc]+parent1[constGenesLoc+constGenes:]]
    #child2[0:constGenes] = parent2Copy[constGenesLoc:constGenesLoc+constGenes]
    child2[constGenesLoc:constGenesLoc + constGenes] = parent2Copy[constGenesLoc:constGenesLoc + constGenes]
    parent2ReducedIndex = [city.index for city in parent2[:constGenesLoc]+parent2[constGenesLoc+constGenes:]]

    parent1Reduced = [city for city in parent2Copy if city.index in parent1ReducedIndex]
    parent2Reduced = [city for city in parent1Copy if city.index in parent2ReducedIndex]

    child1[:constGenesLoc] = parent1Reduced[:constGenesLoc]
    child1[constGenesLoc+constGenes:]=parent1Reduced[constGenesLoc:]
    child2[:constGenesLoc] = parent2Reduced[:constGenesLoc]
    child2[constGenesLoc+constGenes:]=parent2Reduced[constGenesLoc:]


    child1 = Route(child1)
    child2 = Route(child2)
    #print("PARENT COSTS: ",route1.cost,route2.cost)
    #print("CHILD COSTS: ",child1.cost,child2.cost)
    return child1, child2