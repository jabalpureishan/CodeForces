tests = int(input())
for i in range(tests):
    n,k,x = map(int,input().split())
    Min = (k*(k+1))//2
    Max = (n*(n+1))//2 - ((n-k)*((n-k)+1))//2
    if x in range(Min,Max+1):
        print("YES")
    else:
        print("NO")