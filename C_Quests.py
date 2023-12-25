from sys import stdin
input = stdin.readline
def solve(arr1,arr2,n,m):
    ans = float("-inf")
    Max2 = arr2[0]
    sum_ = 0
    for i in range(min(n,m)):
        sum_ += arr1[i]
        Max2 = max(Max2,arr2[i])
        ans = max(ans,sum_ + Max2*(m-i-1))
    return ans



        



for i in range(int(input())):
    
    n,m = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    print(solve(arr1,arr2,n,m))
