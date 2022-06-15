import numpy as np
import pandas as pd
import time
from copy import deepcopy
import imageio
import os
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from SystemObjects.Generations import Generation
from GeneticAlgorithm.GA_Functions import OrderCrossover
from Greedy.greedy_function import GreedySolutionSA
from Greedy.greedy_function import GreedySolutionGA
import matplotlib.pyplot as plt

startTime = time.time()
path = "/Users/suyogkapsikar/PycharmProjects/TSP/Data/"
#path = "Data/"
Data = pd.read_csv(path+"cordinates.csv")
#print(Data.iloc[0][2])

generation = []
#tour,costzz = GreedySolutionSA(Data)
#bestTourEver = deepcopy(tour)

for i in range(0,48):
    tour,costzz = GreedySolutionGA(Data,i+1)
    generation.append(tour)
bestTourEver = deepcopy(tour)
"""
generation1=[]
for tour in generation:
    dummy = deepcopy(tour)
    dummy.GASwapRand()
    dumm2 = deepcopy(tour)
    dumm2.GASwapRand()
    #print(dummy.cost,dumm2.cost)
    generation1.append(dummy)
    generation1.append(dumm2)
generation=generation+generation1
"""
"""
t2 = deepcopy(tour)
#for i in range(500):
t2.GASwapRand()
c1,c2=OrderCrossover(tour,t2)
print(tour.indexList)
print(c1.indexList)#[:12]+c2.indexList[36:])
print(t2.indexList)
print(c2.indexList)#[:12]+c1.indexList[36:])
"""
"""
tour,costzz = GreedySolutionSA(Data)
bestTourEver = deepcopy(tour)
print("Is Greedy Feasible?: ",tour.IsFeasible)

print("Greedy Cost is: ",bestTourEver.cost)

for i in range(100):
    dummy = deepcopy(tour)
    dummy.GASwapRand()
    tour.SwappedRoute()
    generation.append(dummy)
#print("AAAAAAAA",len(generation)==len(set(generation)))
"""
generation = Generation(generation)
print(len(generation.TourList))
Cost = [generation.bestCost]
generationNext = generation
print(len(generationNext.TourList))
fileNames =[]
n=2000
MutationProbability = 0.7
for i in range(n):
    generationNext1 = deepcopy(generationNext)
    generationNext = generationNext1.NextGeneration()
    if bestTourEver.cost > generationNext.bestCost:
        bestTourEver = deepcopy(generationNext.bestTour)
    Cost.append(generationNext.bestCost)
    if i%50==0:
        #print(generationNext.costList[0:5])
        fileName = str(i) + ".png"
        fileNames.append(fileName)
        generationNext.bestTour.SaveRoutePNG(fileName,"GA")
        print(generationNext.bestCost,bestTourEver.cost,generationNext.costList.mean(),len(set(generationNext.costList)),i)

    if np.random.rand() <= MutationProbability:
        generationNext.Mutate()

with imageio.get_writer('GA.gif', mode='I') as writer:
    for filename in fileNames[:-1]:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files
for filename in set(fileNames):
    os.remove(filename)

bestTourEver.SaveRoutePNG('bestSolution.png',"GA")

endTime = time.time()
print("current cost is:"+str(generationNext.bestCost)+". best cost ever is:"+str(bestTourEver.cost))
print("Is the best route feasible?: ",bestTourEver.IsFeasible)
print(bestTourEver.indexList)
print("Time for 100 itr in sec is ",endTime-startTime)
plt.plot(Cost)
plt.show()
plt.plot(Cost)
plt.savefig("CostReduction.png")
