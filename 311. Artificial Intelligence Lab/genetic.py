import random

def genRandList():
    return [random.randint(0, 1) for _ in range(10)]

def genPopulation():
    return [genRandList() for _ in range(20)]

def crossOver(chromosome1, chromosome2):
    listC = chromosome1[0:5] + chromosome2[5:]
    listD = chromosome1[5:] + chromosome2[0:5]
    return [listC, listD]

def mutation(chromosome):
    probability = 0.0005  # Adjusted probability to 0.05%
    res = random.random()
    index = random.randint(0, 9)

    if res < probability:
        chromosome[index] ^= 1

def generation():
    parent = genPopulation()

    for _ in range(25):
        childPopulation = []
        mutatedPopulation = []

        for i in range(len(parent)-1):
            childPopulation.append(crossOver(parent[i], parent[i+1]))

        for childPop in childPopulation:
            mutation(childPop[0])
            mutation(childPop[1])
            mutatedPopulation.extend(childPop)

        parent = mutatedPopulation

def main():
    c1 = genRandList()
    print(c1)
    mutation(c1)
    print(c1)

if __name__ == "__main__":
    main()
    generation()
    
