def solve(n,arr):
    for i in range(n):
        arr[i] = 2**(arr[i])
    return arr












tests = int(input())
for i in range(tests):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))

