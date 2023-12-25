from sys import stdin
input = stdin.readline
def solve(arr,n):
    ans = [0]*(n+1)
    Max = 0
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            ans[j] += 1
            Max = max(Max,ans[j])
    for i in arr:
        if len(ans)>i:
            ans[i] += 1
            Max = max(Max,ans[i])
    return Max


for i in range(int(input())):
    
    n = int(input())
    #s = input()
    arr = list(map(int,input().split()))
    #a,b = map(int,input().split())
    print(solve(arr,n))
