def distancia(lista1, lista2):
    sum = 0

    for i in range(len(lista1)):
        sum+=((lista2[i]-lista1[i])**2)

    return (sum)**(1/2)

def cercanos(puntos, centros):
    pass

def centros(lista):
    pass

def k_means(puntos):
    pass

if __name__ == "__main__":
    lista1 = [1,2,3]
    lista2 = [4,5,6]
    print(f"La distancia entre las listas es: {distancia(lista1,lista2)}")
