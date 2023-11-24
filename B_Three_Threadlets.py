from collections import Counter
def solve():
    array = list(map(int,input().split()))

    arr = {}
    for i in array:
        arr[i] = arr.get(i,0) + 1
    arr = sorted(arr.items(),key=lambda x:x[0])
    arr = dict(arr)    
    count = 0
    while len(arr)>1 and count<3:
        fMax = max(arr,key=lambda x:arr[x])
        Max = max(arr)
        temp = Max - fMax
        temp2 = Max - temp
        if Max!=fMax:
            arr[temp] = arr.get(temp,0) + 1
            arr[temp2] = arr.get(temp2,0) + 1
        else:
            arr[Max//2] = arr.get(Max//2,0) + 1
            arr[Max - Max//2] = arr.get(Max - Max//2,0) + 1
        if 0 in arr:
            arr.pop(0)
        arr[Max] -= 1
        if arr[Max]==0:
            arr.pop(Max)

        #print(arr)
        count += 1
    if len(arr)==1:
        return "YES"
    else:
        return "NO"




for i in range(int(input())):
    print(solve())
    #print("--------------------------")
