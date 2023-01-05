def tableau():
    l = ["pomme","cerise","orange","melon"]
    x = l[0]
    l[0] = l[3]
    l[3] = x
    print(l)

tableau()