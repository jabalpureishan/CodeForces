tests = int(input(""))
while(tests>0):
    tests -= 1
    length,diff = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort()
    array.append(float("inf"))
    Max = 0
    count = 1
    for i in range(1,length+1):
        #print("array[i]:",array[i],"array[i-1]",array[i-1])
        if (array[i]-array[i-1])<=diff:
            
            count += 1
            #print("alloweed count:",count)
        else:
            
            Max = max(Max,count)
            #print("not alloweed max:",Max)
            count = 1
    print(length-Max)
