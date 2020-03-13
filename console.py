from repository import *
from service import *

if __name__ == '__main__':
    fileName=input("Dati numele fisierului:")+".txt"
    repository=RutaRepository(fileName)
#     # # repository.readFromFile()
#     # for line in repository.findAll():
#     #     for col in line:
#     #         print(col)
#     #     print()
    service=RutaService(repository)
    print(service.writeToFile())