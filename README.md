# Grupo10SemanaTec
Repostorio para analizar el database de Iris utilizando machine learning
a través de clusters y la técnica de K-means

Dentro del repositorio se pueden encontrar tres archivos py para realizar
realizar el k_means, cada uno tiene una función distinta pero se conectan
de regreso al correr k_means.py

## io_utilities.py
Este archivo se usa para formatear la base de datos en la forma de una lista de
listas

## visualizations.py
Este archivo grafica los clusters y los centros en un momento particular
También salva las graficas en formato de imágen png dentro de un folder

## k_means.py
Este archivo implementa la técnica de k-means a través de varias funciones

### distancia
La función distancia encuentra la métrica de distancia euclidiana entre los puntos y los centros

### cercanos
La función cercanos encuentra cual centro está más cerca de cada punto y los organiza en una lista correspondiente

### find_centros
La función find_centros crea una lista y la llena con los promedios de cada fila de los clusters

### k_means
La función k_means genera k (cantidad de clusters) centros aleatoriamente utilizando los puntos
Esta función también corre todas las iteraciones, actualizando los centros y puntos correspondientes cada vez, llamando a la función show_clusters_centroids de visualizations.py para graficarlo en cada iteracion

#### Resultados
