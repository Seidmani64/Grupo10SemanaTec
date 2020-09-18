import numpy as np

def distancia(lista1, lista2):
    sum = 0

    for i in range(len(lista1)):
        sum+=((lista2[i]-lista1[i])**2)

    return np.sqrt(sum)

def cercanos(puntos, centros):
    pass
    #list = []
    #for i in range(len(centros)):
        #newList = []
        #list.append(newList)
    #for i in range(len(puntos)):


def centros(lista):
    centrosList = []
    for i in range(len(lista)):
        centrosList.append(np.average(lista[i]))
    return centrosList

def k_means(puntos):
    random.seed(None)
    centrosList = []
    k = input("Enter the value for k: ")
    for i in range(k):
        centrosList.append(puntos[randint(0,len(puntos)-1)])
    for j in range(100):
        centros(cercanos(puntos,centrosList))

if __name__ == "__main__":
    #lista1 = [1,2,3]
    #lista2 = [4,5,6]
    #print(f"La distancia entre las listas es: {distancia(lista1,lista2)}")
    #lista = [[1,2,3],[4,5,6]]
    #print(f"Los centros son: {centros(lista)}")
