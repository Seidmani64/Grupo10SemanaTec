import numpy as np

def distancia(lista1, lista2):
    sum = 0

    for i in range(len(lista1)):
        sum+=((lista2[i]-lista1[i])**2)

    return np.sqrt(sum)

def cercanos(puntos, centros):
    clusters = [[] for f in centros]

    for i, punto in enumerate(puntos):
        point_to_centroids = []
        for j, centro in enumerate(centros):
            point_to_centroids.append(distancia(punto, centros))
        smallest = np.argmin(point_to_centroids)
        clusters[smallest].append(punto)

    return clusters


def centros(lista):
    centrosList = []
    for i in range(len(lista)):
        centrosList.append(np.average(lista[i]))
    return centrosList

def k_means(puntos, k):
    random.seed(None)
    centrosList = []
    for i in range(k):
        centrosList.append(puntos[randint(0,len(puntos)-1)])
    for j in range(10):
        centrosList = centros(cercanos(puntos,centrosList))

if __name__ == "__main__":
    #lista1 = [1,2,3]
    #lista2 = [4,5,6]
    #print(f"La distancia entre las listas es: {distancia(lista1,lista2)}")
    #lista = [[1,2,3],[4,5,6]]
    #print(f"Los centros son: {centros(lista)}")
