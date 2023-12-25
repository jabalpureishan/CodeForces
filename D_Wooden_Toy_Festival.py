from sys import stdin
from math import ceil
input = stdin.readline
def solve(arr,n):
    if n<=3:
        return 0
    arr.sort()
    Min = float("inf")
    i,j = 0,n-1
    while j>=i:
        arrlj = (arr[-1]+arr[min(n-1,j+1)])//2
        arrij = (arr[j]+arr[i+1])//2
        arrsi = (arr[i]+arr[0])//2
        Min = min(Min,max(abs(arr[-1]-arrlj),abs(arr[min(n-1,j+1)]-arrlj),abs(arr[j]-arrij),abs(arr[i+1]-arrij),abs(arr[i]-arrsi),abs(arr[0]-arrsi)))
        if arrsi>arrlj:
            j -= 1
        else:
            i += 1
    return ceil(Min)


for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr,n))
