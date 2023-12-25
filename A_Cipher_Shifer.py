from sys import stdin
input = stdin.readline
def solve(n,s):
    p1,p2,ans = 0,1,""
    while p1<p2 and p2<n:
        if s[p1]==s[p2]:
            ans += s[p2]
            p1 = p2+1
            p2 = p1 +1
        else:
            p2 += 1
    return ans



for i in range(int(input())):
    #arr = list(map(int,input().split()))
    n = int(input())
    s = input()
    #a,b = map(int,input().split())
    print(solve(n,s))


