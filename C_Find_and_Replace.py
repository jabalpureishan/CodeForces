from sys import stdin
input = stdin.readline
def solve(n,s):
    d = {}
    for i in range(n):
        if s[i] not in d:
            d[s[i]] = i%2==0
        elif (i%2==0)!=d[s[i]]:
            return "NO"
    return "YES"



for i in range(int(input())):
    n = int(input())
    s = input()
    #a,b = map(int,input().split())
    print(solve(n,s))
