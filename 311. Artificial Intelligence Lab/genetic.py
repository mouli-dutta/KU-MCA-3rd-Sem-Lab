import random

def genRandList():
    list = []
    for i in range(1, 11):
        list.append(random.randint(0, 1))
    return list

def genPopulation():
    population = []
    for i in range(1, 21):
        population.append(genRandList())
    return population


def crossOver(chromosome1, chromosome2):
    listC = chromosome1[0:5] + chromosome2[5:]
    listD = chromosome1[5:] + chromosome2[0:5]
    
    return [listC, listD]


def mutation(chromosome):
    probability = 0.05
    res = random.random()
    #print("random res", res)

    index = random.randint(0, 9)

    if (res < probability):
        original = chromosome[index]
        #print("original", original)
        flip = original ^ 1
        chromosome[index] = flip

        #print("chrom[inx]", chromosome[index])


def generation():
    parent = genPopulation()
    childPopulation = []
    mutatedPopulation = []

    for i in range(25):

        for i in range(len(parent)-1):
            childPopulation.append(crossOver(parent[i], parent[i+1]))

        for childPop in childPopulation:
            mutation(childPop)
            mutatedPopulation.append(childPop)
        
        parent = mutatedPopulation



def main():
    c1 = genRandList()
    print(c1)
    mutation(c1)
    print(c1)

main()
