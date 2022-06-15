import numpy as np
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
def greedyFunction(StartCity,AllCities):
    AllowedCities = AllCities.copy()
    AllowedCities.remove(StartCity)
    VisitedCities = [StartCity]
    curretCity = StartCity
    while len(AllowedCities)!=0:
        DistList = np.array([StartCity.dist(city) for city in AllowedCities])
        curretCity = AllowedCities[np.argmin(DistList)]
        VisitedCities.append(curretCity)
        AllowedCities.remove(curretCity)
    tour = [city.index for city in VisitedCities]
    cost = sum([VisitedCities[i].dist(VisitedCities[i+1]) for i in range(len(VisitedCities)-1)])+ VisitedCities[-1].dist(VisitedCities[0])
    return VisitedCities, cost
    #return cost

def GreedySolution(Data):
    AllCities = [Node(Data.iloc[i][0],Data.iloc[i][1],Data.iloc[i][2]) for i in range(len(Data))]
    Cost = []
    idx = []
    bestCost = 9*10**99
    bestTour = AllCities
    for city in AllCities:
        tour,cost = greedyFunction(city,AllCities)
        Cost.append(cost)
        idx.append(city.index)
        if bestCost > cost:
            bestCost = cost
            bestTour = tour
    print(idx)
    return bestTour,Cost

def GreedySolutionSA(Data):
    AllCities = [Node(Data.iloc[i][0],Data.iloc[i][1],Data.iloc[i][2]) for i in range(len(Data))]
    Cost = []
    idx = []
    bestCost = 9*10**99
    bestTour = AllCities
    for city in AllCities:
        tour,cost = greedyFunction(city,AllCities)
        Cost.append(cost)
        idx.append(city.index)
        if bestCost > cost:
            bestCost = cost
            bestTour = tour
    cost=min(Cost)
    Tour = Route(bestTour)
    return Tour,Cost

def GreedySolutionGA(Data,NodeIndex):
    AllCities = [Node(Data.iloc[i][0],Data.iloc[i][1],Data.iloc[i][2]) for i in range(len(Data))]
    Cost = []
    idx = []
    bestCost = 9*10**99
    bestTour = AllCities
    #for city in AllCities:
    city = AllCities[NodeIndex-1]
    tour,cost = greedyFunction(city,AllCities)
    Cost.append(cost)
    idx.append(city.index)
    if bestCost > cost:
        bestCost = cost
        bestTour = tour
    cost=min(Cost)
    Tour = Route(bestTour)
    return Tour,Cost