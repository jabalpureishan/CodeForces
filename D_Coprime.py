from sys import stdin
from math import gcd
input = stdin.readline
def solve(arr,n):
    for i in range(n-1,1,-1):
        for j in range(i-1,0,-1):
            if 


for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int,input().split()))
    #s = input()
    #a,b = map(int,input().split())
    print(solve(arr,n))
