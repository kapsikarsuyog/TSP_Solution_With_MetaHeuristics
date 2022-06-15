import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt
from SystemObjects.Nodes import Node
class Route:
    def __init__(self,path):
        self.path = path
        self.links = len(self.path)
        self.cost = sum([self.path[i].dist(self.path[i + 1]) for i in range(len(self.path) - 1)]) + self.path[-1].dist(self.path[0])
        self.indexList = indexList = [city.index for city in self.path]
        self.IsFeasible = len(indexList)==len(set(indexList))

    def GetSwapLen(self):
        NodeNums = self.links
        nums = np.array([i for i in range(NodeNums)])
        den = sum([i for i in range(NodeNums + 1)])
        distrib = np.array([(NodeNums - k) / den for k in nums])
        cdf = np.array([sum(distrib[0:i + 1]) for i in range(len(distrib) - 1)])
        swap = np.random.random()
        cdfbool = cdf >= swap
        if len(np.where(cdfbool == True)[0])>0:
            return np.where(cdfbool == True)[0][0] + 1
        else:
            return 1

    def GetNextSwapPositions(self):
        NodeNums = self.links
        SwapLen = self.GetSwapLen()
        # print(SwapLen)
        SwapStartLoc = np.random.randint(NodeNums)
        SwapEndLoc = SwapStartLoc + SwapLen if SwapStartLoc + SwapLen < NodeNums else SwapStartLoc + SwapLen - NodeNums
        return SwapStartLoc, SwapEndLoc

    def SwappedRoute(self):
        SwapStartLoc, SwapEndLoc = self.GetNextSwapPositions()
        swap1 = deepcopy(self.path[SwapStartLoc])
        swap2 = deepcopy(self.path[SwapEndLoc])
        self.path[SwapStartLoc] = swap2
        self.path[SwapEndLoc] = swap1
        self.cost = sum([self.path[i].dist(self.path[i + 1]) for i in range(len(self.path) - 1)]) + self.path[-1].dist(self.path[0])
        self.indexList = indexList = [city.index for city in self.path]
        self.IsFeasible = len(indexList) == len(set(indexList))

    def GASwapRand(self):
        #This if used only for preparing the initial population for GA implementation
        #This swaps solution in such way that the new solution very very different from the orginal one
        for i in range(50):
            positionA = np.random.randint(0,len(self.path))
            positionB = np.random.randint(0, len(self.path))
            nodeA = deepcopy(self.path[positionA])
            nodeB = deepcopy(self.path[positionB])
            self.path[positionA]=nodeB
            self.path[positionB]=nodeA
        self.cost = sum([self.path[i].dist(self.path[i + 1]) for i in range(len(self.path) - 1)]) + self.path[-1].dist(self.path[0])
        self.indexList = indexList = [city.index for city in self.path]
        self.IsFeasible = len(indexList) == len(set(indexList))

    def SaveRoutePNG(self,name,algo):
        X = [city.x for city in self.path]
        Y = [city.y for city in self.path]
        bestIndex = [city.index for city in self.path]
        XR = deepcopy(X)
        YR = deepcopy(Y)
        XR.append(self.path[0].x)
        YR.append(self.path[0].y)
        plt.scatter(X, Y, s=5)
        for i in range(len(X)):
            plt.annotate(bestIndex[i], (X[i], Y[i] + 0.2))
        plt.plot(XR, YR)
        title = str(algo)+"  TSP with Cost "+str(int(self.cost))
        plt.title(title)
        plt.savefig(name)
        plt.clf()