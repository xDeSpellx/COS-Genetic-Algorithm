from random import randint,random
from math import cos
from math import pi

#Mutation
def mutation(child,probability,Bits):
    points = Bits*probability
    bits = int(points)
    rest = points-bits

    if (random()<rest):
        bits +=1

    for i in range(0,bits):
        pos = randint(1,bits)
        if (child[pos]== 0):
            child[pos]=1
        else:
            child[pos]=0
    return child

#String To Int Converter
def stringToInt(parent):
    parentString = ""
    power = 0
    fin = 0
    for digit in parent[::-1]:
        pow = 2**power
        fin += pow*digit
        power += 1
    return fin

#Crossover
def crossover(child1,child2,Bits):
    position = randint(1,Bits)
    return (child1[0:position] + child2[position:Bits] )

#Genotype To Phenotype
def genoToPheno(parent,Bits):
    phenotype = stringToInt(parent)
    return((phenotype/((2**Bits)-1))*2*pi)

# Find the best
def findBest(fitList):
    return fitList.index(max(fitList))

#Fitness Function
def fitness(parent,Bits):
    return(cos(genoToPheno(parent,Bits)))

#Roulette
def Roulette(FitnessList):
    sum=0
    sum2=0
    SumRnd = 0
    for fit in FitnessList:
        sum+=fit+1
    SumRnd = random()*sum

    for fit in FitnessList:
        sum2+=fit+1
        if (sum2>SumRnd):
            break;
    return (FitnessList.index(fit))

