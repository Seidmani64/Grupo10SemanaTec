import numpy as np

def distancia(lista1, lista2):
    sum = 0

    for i in range(len(lista1)):
        sum+=((lista2[i]-lista1[i])**2)

    return np.sqrt(sum)

def cercanos(puntos, centros):
    list = []
    for x in range(len(centros)):
        newList = []
        list.append(newList)

def centros(lista):
    centrosList = []
    for i in range(len(lista)):
        centrosList.append(np.average(lista[i]))
    return centrosList

def k_means(puntos):
    pass

if __name__ == "__main__":
    #lista1 = [1,2,3]
    #lista2 = [4,5,6]
    #print(f"La distancia entre las listas es: {distancia(lista1,lista2)}")
    #lista = [[1,2,3],[4,5,6]]
    #print(f"Los centros son: {centros(lista)}")
