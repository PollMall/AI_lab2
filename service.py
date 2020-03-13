from repository import *


class RutaService:
    def __init__(self, repository):
        self.__repository = repository

    def findAll(self):
        return self.__repository.findAll()

    def findOne(self, ruta):
        return self.__repository.findOne(ruta)

    def save(self, ruta):
        self.__repository.save(ruta)

    def __greedy(self, src=0, dest=-1):
        parcurse = self.__det_drum_minim(src, dest)
        print(parcurse)
        cost = self.__det_lung_drum(parcurse)
        if dest == -1:
            cost = cost + ((self.__repository.findAll())[parcurse[-1]][parcurse[0]]).getDist()
        print(cost)
        return (parcurse, cost)

    def __det_drum_minim(self, src, dest):
        matrix = self.__repository.findAll()
        parcurse = [src]
        while (len(parcurse) != self.__repository.getNrOfCities()) and (parcurse[-1] != dest):
            # min = max(matrix[parcurse[-1]])
            min = (max(matrix[parcurse[-1]])).getDist()
            # min_index = 0

            for i in range(len(matrix[parcurse[-1]])):
                if (matrix[parcurse[-1]][i]).getDist() == min:
                    # min = matrix[parcurse[-1]][i].getDist()
                    min_index = i
                    break
            for j in range(len(matrix[parcurse[-1]])):
                if (matrix[parcurse[-1]][j].getDist() < min) and (j not in parcurse) and (
                        matrix[parcurse[-1]][j].getDist() != 0):
                    min = matrix[parcurse[-1]][j].getDist()
                    min_index = j
            parcurse.append(min_index)
        # parcurse.append(max(parcurse)+1)
        return parcurse

    def __det_lung_drum(self, parcurse):
        sum = 0
        matrix = self.__repository.findAll()
        for i in range(len(parcurse) - 1):
            sum = sum + (matrix[parcurse[i]][parcurse[i + 1]]).getDist()
        return sum

    def writeToFile(self):
        # fileName=(self.__repository.getFileName().split(".txt"))[0]
        # fileName=fileName+"_solution.txt"
        # fileName=self.__repository.getFileName().replace(".txt","_solution.txt")

        fileName = self.__repository.getFileName().replace(".txt", "_solution.txt")
        sol1 = self.__greedy()
        sol2 = self.__greedy(self.__repository.getSrc(), self.__repository.getDest())

        with open(fileName, "w") as file:
            file.write(str(self.__repository.getNrOfCities()) + "\n")
            parcurse=sol1[0]
            cost=sol1[1]
            for i in range(len(parcurse) - 1):
                file.write(str(parcurse[i]+1) + ",")
            file.write(str(parcurse[-1]+1) + "\n" + str(cost)+"\n")
            parcurse = sol2[0]
            cost = sol2[1]
            file.write(str(len(parcurse))+"\n")
            for i in range(len(parcurse) - 1):
                file.write(str(parcurse[i]+1) + ",")
            file.write(str(parcurse[-1]+1) + "\n" + str(cost)+"\n")
