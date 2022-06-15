import numpy as np
import pandas as pd
import time
from copy import deepcopy
import imageio
import os
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from SimulatedAnnealingFunctions import OneStepAnnealing
from Greedy.greedy_function import GreedySolutionSA
import matplotlib.pyplot as plt

startTime = time.time()
path = "/Users/suyogkapsikar/PycharmProjects/TSP/Data/"
#path = "Data/"
Data = pd.read_csv(path+"cordinates.csv")
#print(Data.iloc[0][2])
Cost = []
bestTour,cost = GreedySolutionSA(Data)
bestTourEver = bestTour
Temperature = min(cost)/2
print(Temperature)
imagePath = "/PNGs/"
fileNames=[]

for i in range(75000):
    TempTour = deepcopy(bestTour)
    TempTour.SwappedRoute()
    #print(bestTour.cost,TempTour.cost)
    bestTour = OneStepAnnealing(bestTour,TempTour,Temperature)
    if i % 100 == 0:
        Cost.append(bestTour.cost)

    if i % 1000 == 0:
        fileName = str(i)+".png"
        fileNames.append(fileName)
        bestTour.SaveRoutePNG(fileName,"SA")

    if i % 1500==0 and i!=0:
        Temperature /= 1.2
    print(bestTour.cost, TempTour.cost,i,Temperature) if i%100==0 else None
    if bestTourEver.cost > bestTour.cost:
        bestTourEver = bestTour

endTime = time.time()
print("Time for 100 itr in sec is ",endTime-startTime)
print("Best Cost is ",bestTour.cost)
print("best Cost Ever ",bestTourEver.cost)
#plt.plot(Cost)
#plt.show()

X = [city.x for city in bestTourEver.path]
Y = [city.y for city in bestTourEver.path]
#bestIndex = [city.index for city in bestTourEver.path]
XR = deepcopy(X)
YR = deepcopy(Y)
XR.append(bestTourEver.path[0].x)
YR.append(bestTourEver.path[0].y)
#plt.scatter(X,Y,s=5)
#for i in range(len(X)):
#    plt.annotate(bestIndex[i], (X[i], Y[i] + 0.2))
#plt.plot(XR,YR)
#plt.show()
#print(bestIndex)
# build gif

for j in range(500000,500025):
    fileName = str(j) + ".png"
    fileNames.append(fileName)
    bestTourEver.SaveRoutePNG(fileName,"ACO")

with imageio.get_writer('SA_gif.gif', mode='I') as writer:
    for filename in fileNames:
        image = imageio.imread(filename)
        writer.append_data(image)




# Remove files
for filename in set(fileNames):
    os.remove(filename)

print("Is the best route feasible?: ", bestTourEver.IsFeasible)
bestTourEver.SaveRoutePNG("BestRoute.png","SA")
endTime = time.time()
print("Time for 100 itr in sec is ",endTime-startTime)
plt.scatter(X,Y,s=5)
for i in range(len(X)):
    plt.annotate(bestTourEver.indexList[i], (X[i], Y[i] + 0.2))
plt.plot(XR,YR)
plt.show()
print(bestTourEver.indexList)
plt.clf()
plt.plot(Cost)
plt.show()
plt.clf()
plt.plot(Cost)
plt.savefig("Cost over itr.png")
