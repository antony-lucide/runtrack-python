def tableau(L):
    compte = 0
    for i in range(3):
        if(L[i] %3 == 0):
            compte = compte + 1
    print(compte)

L = [8, 24,48,2,16]
tableau(L)