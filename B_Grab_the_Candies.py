from sys import stdin
input = stdin.readline
def solve(arr,n):
    even,odd = 0,0
    for i in arr:
        if i%2==0:
            even += i
        else:
            odd += i
    if even>odd:
        return "YES"
    return "NO"


for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr,n))
