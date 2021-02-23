def bolen(x):
    bolenler = []
    for i in range(1, x+1):
        if (x % i == 0):
            bolenler.append(i)
    print(bolenler)
while True:
    a = input("kanka bi sayi ver bakam bana ")
    if(a == "q"):
        print("iyi gidiom ben ")
        break

    else:
        a = int(a)
        bolen(a)
