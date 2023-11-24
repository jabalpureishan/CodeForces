string = "abcdefghijklmnopqrstuvwxyz"
d = {}
for i in range(1,27):
    d[string[i-1]] = i
tests = int(input())
for i in range(tests):
    length = int(input())
    n = length-1
    arr = []
    for j in range(length):
        arr.append([])
        arr[j].extend(input())
    #print(arr)
    total = 0
    for j in range(length):
        for k in range(length):
            temp = [arr[j][k],arr[k][n-j],arr[n-k][j],arr[n-j][n-k]]
            Max = max(temp)
            for l in temp:
                total += d[Max] - d[l]
            arr[j][k],arr[k][n-j],arr[n-k][j],arr[n-j][n-k] = Max,Max,Max,Max
            
    print(total)
    #print("finnal:",arr)
    #print("-----------------")

