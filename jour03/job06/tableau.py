def tableau():
    k = "abcdefghijklmnopqrstuvwxyz" * 10
    for i in range(15):        
        for b in range(i*2):
            print(k[b], end="") #Pour qu'il aille pas à la ligne
        print("")


tableau()

