def maximum(liste):
    max = liste[0]
    min = liste[0]
    for i in range(len(liste)):
        if(liste[i] > max):
            max = liste[i]
        if(liste[i] < min):
            min = liste[i]
    return(max, min)

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

print(maximum(L))