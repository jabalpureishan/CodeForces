from sys import stdin
input = stdin.readline
def solve(arr,n):
    new = sorted(arr)
    #return new
    if n==1:
        return arr
    ans = []
    for i in arr:
        if i==new[-1]:
            ans.append(new[-1]-new[-2])
        else:
            ans.append(i-new[-1])
    return ans

for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int,input().split()))
    #s = input()
    #a,b = map(int,input().split())
    val = solve(arr,n)
    for i in val:
        print(i,end=" ")
    print()
