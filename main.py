#Genetic algorithm for cos() function
#John Georgoudakis AM:52
#PMS Stin efarmosmeni pliroforiki
from functions import *

####Globals#####
N = 10
Bits = 10
Generations =100
################

ParentsList = []
Parent = [0] * Bits
ParentFit = []

Population = [0] * N
PopulationFitness = [0] * N

#Print Parent Phenotype and Fitness
def Display(parent):
    print("-----Parent-----" + "\t\t\t\t\t---Phenotype(X)---" + "\t\t\t----Solution(Y)----")
    for par in parent:
        print(str(par)+"\t"+ str(genoToPheno(par,Bits)) +"\t"+ str(fitness(par,Bits)))

#Random parents generator
def generateParents():
    for n in range(0, N):
        parentTemp = list(map(lambda _:randint(0,1),Parent)).copy()
        ParentsList.append(parentTemp)
        ParentFit.append(fitness(parentTemp,Bits))
print("Starting Generation")

#Main generation loop
def runGenerations(Generations):
    for generations in range(0, Generations):
        print("===============")
        print("Generation " + str(generations + 1))
        print("===============")
        Population[0] = ParentsList[findBest(ParentFit)]
        PopulationFitness[0] = ParentFit[findBest(ParentFit)]
        #Calculate Children
        for children in range(1, N):
            parent1 = Roulette(ParentFit)
            parent2 = Roulette(ParentFit)

            if (random() < 0.9):
                Population[children] = crossover(ParentsList[parent1], ParentsList[parent2], Bits)
            elif (random() < 0.5):
                Population[children] = ParentsList[parent1]
            else:
                Population[children] = ParentsList[parent2]

            mutation(Population[children], 0.01, Bits)
            PopulationFitness[children] = fitness(Population[children], Bits)
        #Swap Populations
        for i in range(0, N):
            ParentsList[i] = Population[i]
            ParentFit[i] = PopulationFitness[i]

        #Best = findBest(ParentFit)
        Display(ParentsList)
        print("Current solution gives ===> " + str(PopulationFitness[0]))

##MAIN##
#Create Random Parents
generateParents()
Display(ParentsList)
runGenerations(Generations)