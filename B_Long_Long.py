tests = int(input(""))
for i in range(tests):
    length = int(input(""))
    array = list(map(int, input().split()))
    new = []
    Sum = 0
    Nlength = 0
    for i in array:
        Sum += abs(i)
        if i!=0:
            Nlength += 1
            new.append(i)
    count = 0
    for i in range(1,length):
        if array[i]<0 and array[i-1]>0:
            count += 1
    print(Sum,count)

    
    
        

            

