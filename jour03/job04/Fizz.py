def Fiz():
    i = 1
    while( i <= 100):
        if(i%5 == 0 and i%3 == 0):
            print("FizzBuzz")
        elif(i%5 == 0):
            print("Buzz")
        elif(i%3 == 0):
            print("Fizz")
        i = i + 1

Fiz()