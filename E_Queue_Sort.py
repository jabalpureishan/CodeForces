def solve(n,arr):
    Min = arr.index(min(arr))
    new = sorted(arr[Min+1:])
    if new==arr[Min+1:]:
        return Min
    return -1


tests = int(input())
for i in range(tests):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
