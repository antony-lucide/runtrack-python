def fruit(type, saison):
    if(type == "fruits"):
        if(saison == "hiver"):
            print("orange, mandarine et kiwi")
        elif(saison == "été"):
            print("Poire, fraise, cassis")
    elif(type == "légume"):
        if(saison == "hiver"):
            print("carotte, topinambour, endive")
        elif(saison == "été"):
            print("artichaut, aubergine,navet")

fruit("fruits", "hiver")
fruit("légume", "été")