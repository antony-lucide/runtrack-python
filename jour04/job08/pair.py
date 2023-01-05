def tableau(liste):
    somme = 0
    for i in range(len(liste)):
        if(liste[i]%2==0):
            somme = somme + liste[i]
    return (somme)
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

print(tableau(L))