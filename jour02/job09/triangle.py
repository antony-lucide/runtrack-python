def triangle(a, b, c):
    if( a == b and b == c):
        print("Le triangle est équilatéral")
    elif(c * b  and c * a ):
        print("Le triangle est un triangle réctangle")
    elif( c != b  and c == a or b == a):
        print("Le triangle est un triangle isocèle")
    else:
        print("Le triangle est un triangle quelconque")


triangle(1, 2, 1)
