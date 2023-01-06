#Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en
#fonction des paramètres d’entrées, (width, height), par exemple :
#draw_rectangle(10, 3)

def rectangle(hauteur,largeur):
    for i in range(hauteur):
        for x in range(largeur): 
            if(i == 0 or i == hauteur-1):
                print("-",end="")
            elif(x == 0 or x == largeur-1):
                print("|",end="")
            else:
                print(" ", end="")
        print("")





rectangle(10,8)
