tests = int(input(""))
while(tests>0):
    tests -= 1
    responses = int(input(""))
    quality = -1
    ind = 0
    for i in range(responses):
        x,y = map(int, input().split())
        if x>10:
            continue
        else:
            if y>quality:
                quality = y
                ind = i
    print(ind+1) 
            
    