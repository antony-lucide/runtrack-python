
def verification(num):
    x = 2
    for x  in range(2,num):
        if (num%x == 0):
            return False
    return True



def premier ():
    i = 0
    while(i <= 1000):
        if(verification(i)):
            print(i)
        i = i + 1

premier()