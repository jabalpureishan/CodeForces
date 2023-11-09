n = int(input())
arr = []
for  i in range(n):
    arr.append(list(map(int,input().split())))
Max = []
for i in range(n):
        for j in range(n):
            if arr[j][0]>arr[i][0] and arr[j][1]>arr[i][1] and arr[j][2]>arr[i][2]:
                break
        else:
            Max.append(i)
print(min(Max,key=lambda x:arr[x][3])+1)


#print(arr)