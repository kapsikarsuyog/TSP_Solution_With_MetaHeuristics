import numpy as np
import pandas as pd

from SystemObjects.Graphs import Graph
from SystemObjects.Routs import Route
from SystemObjects.Nodes import Node
from copy import deepcopy

class Ants:
    def __init__(self, AntIndex,allowedNodes):
        self.AntIndex = AntIndex
        self.currNode = None
        self.allowedNodes = deepcopy(allowedNodes)
        self.visitedNodes = []

    def OneStep(self,graph,alpha,beta):
        graphindex = self.currNode.index - 1
        selection = []
        for city in self.allowedNodes:
            measur = (graph.PheroMatrix[graphindex][city.index-1])**alpha * (1/graph.DistMatrix[graphindex][city.index-1])**beta
            selection.append(measur)
        probability = np.array(selection)/sum(selection)
        NextCity = np.random.choice(self.allowedNodes,p=probability)
        self.currNode = NextCity
        self.visitedNodes.append(NextCity)
        self.allowedNodes.remove(NextCity)

    def fullRoute(self,graph,startLoc,alpha,beta):
        if len(self.visitedNodes)!=0:
            raise Exception("Something is wrong, Visted city list is not empty")
        #startLoc = np.random.randint(1,48)
        self.currNode = self.allowedNodes[startLoc]
        self.allowedNodes.remove(self.currNode)
        self.visitedNodes.append(self.currNode)
        zzchk = 0
        while len(self.allowedNodes)!=0:
            self.OneStep(graph,alpha,beta)
            zzchk+=1
            if zzchk >= 48:
                raise Exception("Full Route Function is running beyond 48 iteration")
        self.routeTaken = Route(self.visitedNodes)

    def pheroDeposition(self,Q,allowedNodes):
        if len(self.allowedNodes)!=0:
            raise Exception("Something is wrong, Allowed city list is not empty")
        deltaPhero = np.zeros((len(self.routeTaken.path),len(self.routeTaken.path)))
        for i in range(len(self.routeTaken.indexList)-1):
            #print("i",i,[self.routeTaken.indexList[i]-1,self.routeTaken.indexList[i+1]-1])
            deltaPhero[self.routeTaken.indexList[i]-1][self.routeTaken.indexList[i+1]-1] = Q/self.routeTaken.cost
            deltaPhero[self.routeTaken.indexList[i+1]-1][self.routeTaken.indexList[i]-1] = Q/self.routeTaken.cost

        deltaPhero[self.routeTaken.indexList[-1] - 1][self.routeTaken.indexList[-1 + 1] - 1] = Q / self.routeTaken.cost
        deltaPhero[self.routeTaken.indexList[-1 + 1] - 1][self.routeTaken.indexList[-1] - 1] = Q / self.routeTaken.cost
        #print(pd.DataFrame(deltaPhero))
        #print("1st",sum(pd.DataFrame(deltaPhero).iloc[0]))
        #print("Last 47",self.routeTaken.indexList[-1]-1, sum(pd.DataFrame(deltaPhero).iloc[self.routeTaken.indexList[-1]-1]))
        #print("Last 47",self.routeTaken.indexList[0]-1, sum(pd.DataFrame(deltaPhero).iloc[self.routeTaken.indexList[0] - 1]))
        #for i in range(len(deltaPhero)):
        #    print(str(i),sum(pd.DataFrame(deltaPhero).iloc[i]))
        #print("Cost Routr: ",self.routeTaken.cost)
        self.visitedNodes=[]
        self.allowedNodes = deepcopy(allowedNodes)
        return deltaPhero