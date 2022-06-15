import numpy as np
import pandas as pd
#Mean Distace is 3216
#Initial Pheromore shuld be 3216 on each link
#Q SHOULD BE 3200**2

class Graph:
    def __init__(self,Data):
        DistMat = np.zeros((len(Data),len(Data)))
        for i in range(len(Data)):
            for j in range(len(Data)):
                if i == j:
                    DistMat[i, j] = 999999
                else:
                    DistMat[i, j] = np.sqrt((Data["long"][i] - Data["long"][j]) ** 2 + (Data["lat"][i] - Data["lat"][j]) ** 2)
        self.DistMatrix = DistMat

    def resetPheromore(self,Q):
        self.PheroMatrix = np.zeros((len(self.DistMatrix),len(self.DistMatrix))) + np.sqrt(Q)

    def evaporatePhero(self,evapRate):
        TempPhero = self.PheroMatrix*(1-evapRate)
        self.PheroMatrix = TempPhero

    def updatePhero(self,deltaMat):
        if(deltaMat.shape != self.PheroMatrix.shape):
            raise Exception("Shaped delta matrix is not same as shape of existing Pheromore matrix")
        self.PheroMatrix+=deltaMat

"""
path = "/Users/suyogkapsikar/PycharmProjects/TSP/Data/"
#path = "Data/"
Data = pd.read_csv(path+"cordinates.csv")
dist = np.zeros((len(Data),len(Data)))
for i in range(len(Data)):
    for j in range(len(Data)):
        if i==j:
            dist[i,j]=999999
        else:
            dist[i,j] = np.sqrt((Data["long"][i]-Data["long"][j])**2 + (Data["lat"][i]-Data["lat"][j])**2)
print(dist)
print(dist.mean())
"""