import numpy as np

from io_utilities import load_data
from visualizations import show_clusters_centroids

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
            point_to_centroids.append(distancia(punto, centro))
        smallest = np.argmin(point_to_centroids)
        clusters[smallest].append(punto)

    return clusters


def find_centros(clusters):
    centrosList = []
    for i in clusters:
        centrosList.append(np.mean(i, axis = 0))
    return centrosList

def k_means(puntos, k, iterations = 10):
    idx = np.random.randint(len(puntos),size=k)

    centros = puntos[idx,:]
    clusters = cercanos(puntos,centros)

    for i in range(iterations):

        show_clusters_centroids(
                clusters,
                centros,
                "Graph",
            )

        clusters = cercanos(puntos, centros)
        centros = find_centros(clusters)

    return clusters,centros

if __name__ == "__main__":
    data = load_data('./data/iris.data')
    k = 4

    X = np.array([f[:-1] for f in data])
    y = np.array([f[-1] for f in data])

    clusters,centros = k_means(X,k)

    show_clusters_centroids(clusters,centros,"Result",keep=True)
