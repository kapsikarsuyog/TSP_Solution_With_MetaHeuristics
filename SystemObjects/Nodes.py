import math

class Node:
    def __init__(self,idx,x,y):
        self.index = idx
        self.x = x
        self.y = y

    def dist(self,city):
        return math.sqrt((self.x-city.x)**2 + (self.y-city.y)**2)


#one = Node(1,0,0)
#two = Node(2,6,8)
#three = Node(3,9,12)
#print(one.dist(two))
#print(three.dist(two))
#print(three.dist(one))
#route = [one,two,three]
#print(route)
#ans = sum([route[i].dist(route[i+1]) for i in range(len(route)-1)])+ route[-1].dist(route[0])
#print(ans)

