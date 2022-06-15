# TSP_Solution_With_MetaHeuristics
The Symmetric TSP problem of capitals of 48 mainland USA states from [TSPLIB](http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/att48.tsp) has been solved using Greedy Heuristic and three meta heuristic methods i.e. Simulated Annealing, Genetic Algorithm (Order Crossover of genes) and Ant Colony Optimization (ACO).

The entire code is build from scratch, below are the different TSP Solutions generated over the iterations

### Simulated Annealing

![Alt Text](https://raw.githubusercontent.com/kapsikarsuyog/DataStore/main/SA_gif.gif)

### Ant Colony Optimization

![Alt Text](https://raw.githubusercontent.com/kapsikarsuyog/DataStore/main/ACO_gif.gif)

### Genetic Algorithm (Order Crossover)

![Alt Text](https://raw.githubusercontent.com/kapsikarsuyog/DataStore/main/GA.gif)

### Observations

1. For a given problem, *Simulated Annealing* and *ACO* works way better than the genetic algorithm. <br>
2. In Simulated Annealing cost initially fluctuates a lot in higher region than drops gradually as temprature falls. <br>
3. In ACO, Drop is faster than in the Simulated annealing. <br>
4. In ACO only 3 to 6 ants can lead to a good solution in 250 iterations. <br>
5. As far as time is concerned, ACO is the faster for the given problem, gives good solution within 5-10 secs 
