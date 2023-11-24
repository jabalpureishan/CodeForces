def solve(m,k,l,r,c,p):
    if c>k:
        temp = max(k,c-m)
    elif c<k:
        temp  = min(k,c+m)
    else:
        temp = c
    if temp in range(l,r+1):
        return p
    return float("inf")

tests = int(input())
for i in range(tests):
    #arr = list(map(int,input().split()))
    # intvar = int(input())
    # strvar = input()
    n,m,k,l,r = map(int,input().split())
    Min = float("inf")
    for j in range(n):
        c,p = map(int,input().split())
        Min = min(Min,solve(m,k,l,r,c,p))
    if Min == float("inf"):
        print(-1)
    else:
        print(Min)


