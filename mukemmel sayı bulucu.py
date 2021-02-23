def bolen(x):
    bolenler = []
    for i in range(1, x):
        if (x % i == 0):
            bolenler.append(i)
    if(sum(bolenler) == x):
        print(x)
        print(bolenler)
        bolenler = []

for a in range(1,1001):
    bolen(a)
