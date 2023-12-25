from sys import stdin
input = stdin.readline
def solve(arr,n):
    arr.append(-1)
    n += 1
    count = 0
    pind,prev = 0,arr[0]
    for i in range(1,n):
        #print(prev,pind)
        if arr[i]!=prev:
            if (pind==0 or arr[pind-1]>arr[pind]) and (i==n-1 or arr[i-1]<arr[i]):
                count += 1
                #print("count++")
                if count>=2:
                    return "NO"
            pind = i
            prev = arr[i]
        
    if count==1:
        return "YES"
    return "NO"




for i in range(int(input())):
    
    n = int(input())
    #s = input()
    #a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(arr,n))
