import numpy as np
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from GeneticAlgorithm.GA_Functions import OrderCrossover
from copy import deepcopy

class Generation:
    def __init__(self,TourList):
        self.TourList = TourList
        self.costList = np.array([tour.cost for tour in self.TourList])
        self.bestCost = min(self.costList)
        worstCost = max(self.costList)
        self.bestTour = self.TourList[np.argmin(self.costList)]
        #self.pdf = list(1/self.costList/sum(1/self.costList))
        #self.costDistribution = 1/self.costList/sum(1/self.costList)

    """
    def GenSampling(self):
        pdf = (1/self.costList**3)/(sum(1/self.costList**3))
        cdf = np.array([sum(pdf[0:i+1]) for i in range(len(pdf)-1)])
        appendList = deepcopy(self.TourList)
        SampledGen = []
        for i in range(len(self.TourList)):
            randNum = np.random.rand()
            cdfbool = cdf >= randNum
            if len(np.where(cdfbool == True)[0]) > 0:
                SampledGen.append(appendList[np.where(cdfbool == True)[0][0]])
            else:
                SampledGen.append(appendList[0])
        return Generation(SampledGen)
        
        self.TourList = SampledGen
        self.costList = np.array([tour.cost for tour in self.TourList])
        self.bestCost = min(self.costList)
        self.bestTour = self.TourList[np.argmin(self.costList)]
        self.pdf = list(1/self.costList/sum(1/self.costList))
    """

    def BestWorstIndices(self):
        self.bestIndex = np.argmin(self.costList)
        self.worstIndex = np.argmax(self.costList)
        IndexArray = self.costList.argsort()
        self.NextBestIndex = IndexArray[1]
        self.NextWorstIndex = IndexArray[-2]
        #print(self.bestIndex,self.NextBestIndex,self.worstIndex,self.NextWorstIndex)
        #print(self.costList[self.bestIndex],self.costList[self.NextBestIndex],self.costList[self.worstIndex],self.costList[self.NextWorstIndex])


    def NextGeneration(self):
        self.BestWorstIndices()
        NextGen = deepcopy(self.TourList)
        bestTour = deepcopy(self.bestTour)
        NextBestTour = deepcopy(self.TourList[self.NextBestIndex])
        #if bestTour.cost==NextBestTour.cost == self.costList[self.worstIndex]==self.costList[self.NextWorstIndex]:
        #    raise Exception("All Best Worst are the same")
        #elif bestTour.cost==NextBestTour.cost:
        #    raise Exception("best tours are same")
        child1, child2 = OrderCrossover(bestTour,NextBestTour)
        if child1.cost not in [bestTour.cost,NextBestTour.cost]:
            NextGen[self.worstIndex] = child1
        if child2.cost not in [bestTour.cost, NextBestTour.cost]:
            NextGen[self.NextWorstIndex]=child2
        return Generation(NextGen)

    def Mutate(self):
        self.BestWorstIndices()
        MutateLoc = self.NextBestIndex
        MutationRout = deepcopy(self.TourList[MutateLoc])
        MutationRout.SwappedRoute()
        self.TourList[MutateLoc] = MutationRout
        self.costList = np.array([tour.cost for tour in self.TourList])
        self.bestCost = min(self.costList)
        self.bestTour = self.TourList[np.argmin(self.costList)]
        self.pdf = list(1 / self.costList / sum(1 / self.costList))
