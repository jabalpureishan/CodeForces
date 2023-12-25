from sys import stdin
input = stdin.readline
def solve(n):
    ans = n*4 + (n-1) + 3 + (((n-2)*(n-1))//2 - 1)*2
    return ans




for i in range(int(input())):
    #arr = list(map(int,input().split()))
    n = int(input())
    #s = input()
    #a,b = map(int,input().split())
    print(solve(n))
