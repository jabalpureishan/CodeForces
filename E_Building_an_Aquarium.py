tests = int(input(""))
while tests>0:
    tests -= 1
    height,water = input().split()
    height,water = int(height),int(water)
    arr = tuple(map(int,input().split()))
    h = 1
    while True:
        w = 0
        for i in arr:
            w += max(h - i,0)
        #print(w,h)
        if w>water:
            break
        else:
            h += 1
    print(h-1)

