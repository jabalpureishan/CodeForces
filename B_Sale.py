length,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

Sum = ind = 0
while arr[ind]<=0 and ind<m:
    Sum += arr[ind]
    ind += 1
    if ind==length:
        break
print(abs(Sum))
