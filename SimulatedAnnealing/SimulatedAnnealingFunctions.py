import numpy as np
from SystemObjects.Nodes import Node
from SystemObjects.Routs import Route
from copy import deepcopy

def OneStepAnnealing(route1,route2,Temperature):
    if route1.cost > route2.cost:
        currRoute = route2
    else:
        base = np.random.random()
        compare = np.exp(-abs(route1.cost-route2.cost)/Temperature)
        #print(base,compare)
        #currRoute = route2 if base <= compare else currRoute = route1
        if base<=compare:
            currRoute = route2
        else:
            currRoute = route1
    return currRoute