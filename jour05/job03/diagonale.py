def rectangle(taille):
    for i in range(taille):
        for x in range(taille): 
            if(i ==0 or i == taille-1): #tests des coordonnées
                print("-",end="")
            elif(x == 0 or x == taille-1):
                print("|",end="")
            else:
                if(x == taille - i):
                    print(" ", end="")
                else:
                    print("#", end="")
        print("")


rectangle(10)