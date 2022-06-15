import numpy as np
import pandas as pd
import time
from copy import deepcopy
import imageio
import os
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from SystemObjects.Ants import Ants
from SystemObjects.Graphs import Graph
from Greedy.greedy_function import GreedySolutionSA
import matplotlib.pyplot as plt

startTime = time.time()
path = "/Users/suyogkapsikar/PycharmProjects/TSP/Data/"
Data = pd.read_csv(path+"cordinates.csv")
NetworkGraph = Graph(Data)
n=6 #No of ants
Q = 3200**2 * 100
alpha = 1
beta = 1
evapRate = 0.1

NetworkGraph.resetPheromore(Q)
AllowedCities =  [Node(Data.iloc[i][0],Data.iloc[i][1],Data.iloc[i][2]) for i in range(len(Data))]
antList = [Ants(i,AllowedCities) for i in range(n)]
itr = 280
Cost =[]
fileNames=[]

bestTourEver,CostZZ = GreedySolutionSA(Data)

for i in range(itr):
    StartLoc = [i for i in range(len(Data))]
    np.random.shuffle(StartLoc)
    while len(StartLoc)>n:
        StartLoc.pop(-1)

    #print(StartLoc)
    NetworkGraph.evaporatePhero(evapRate)

    j=0
    for ant in antList:
        #print(StartLoc[j],j)
        #print("Allowed Cities",[city.index for city in AllowedCities])
        ant.fullRoute(NetworkGraph,StartLoc[j],alpha,beta)
        #print("Ant Cost",ant.routeTaken.cost)
        j+=1
    Antcost = [ant.routeTaken.cost for ant in antList]
    Cost.append(min(Antcost))
    print(i,min(Antcost),beta,alpha)

    if i%10==0:
        fileName = str(i) + ".png"
        fileNames.append(fileName)
        antList[np.argmin(Antcost)].routeTaken.SaveRoutePNG(fileName,"ACO")


    if i!=0 and i%40==0 and beta<4:
        beta*=1.5
    if beta >3 and i%40==0 and alpha<2:
        alpha *=2

    """
    if i==49:
        alpha = 1
        beta = 2
    elif i==99:
        alpha=1
        beta = 1.5
    elif i==149:
        alpha=1.25
        beta=1
    """

    if bestTourEver.cost > min([ant.routeTaken.cost for ant in antList]):
        bestTourEver = deepcopy(antList[np.argmin(Antcost)].routeTaken)

    for ant in antList:
        deltaPhero = ant.pheroDeposition(Q,AllowedCities)
        NetworkGraph.updatePhero(deltaPhero)

print("Best Cost is: ",min(Cost))
bestTourEver.SaveRoutePNG("BestCost Route","ACO")
print("Time in Sec: ",time.time()-startTime)
plt.plot(Cost)
plt.show()
plt.plot(Cost)
plt.savefig("Cost over itr.png")
plt.clf()

for j in range(1000,1020):
    fileName = str(j) + ".png"
    fileNames.append(fileName)
    bestTourEver.SaveRoutePNG(fileName,"ACO")

with imageio.get_writer('ACO_gif.gif', mode='I') as writer:
    for filename in fileNames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Remove files
for filename in set(fileNames):
    os.remove(filename)

print("Is the best route feasible?: ", bestTourEver.IsFeasible)