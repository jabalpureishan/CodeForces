from sys import stdin
input = stdin.readline
def solve(n,s):
    Max = 0
    for i in s:
        Max = max(Max,ord(i)-96)
    return Max


for i in range(int(input())):
    #arr = list(map(int,input().split()))
    n = int(input())
    s = input()
    #a,b = map(int,input().split())
    print(solve(n,s))
