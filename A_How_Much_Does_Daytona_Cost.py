tests = int(input())
for i in range(tests):
    n,k = map(int,input().split())
    arr = set(map(int,input().split()))
    if k in arr:
        print("YES")
    else:
        print("NO")