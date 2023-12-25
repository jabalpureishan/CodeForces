from sys import stdin
#from sympy import isprime
from math import sqrt
input = stdin.readline
def sie(n):
    arr = [False]*2 + [True]*(n-1)
    root = sqrt(n)
    i = 2
    while i<=root:
        if arr[i]:
            for j in range(i*i,n+1,i):
                arr[j] = False
        i += 1
    return arr
sieve = sie(1000000)
for i in range(int(input())):
    arr = map(int,input().split())
    
    for j in arr:
        if j==1:
            print("NO")
        else:
            root = int(sqrt(j))
            if root*root==j and sieve[root]:
                print("YES")
            else:
                print("NO")            
