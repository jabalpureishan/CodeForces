from sys import stdin
#from sympy import isprime
from math import sqrt
input = stdin.readline
n = int(input())
arr = []
check = [False]*2+[True]*(n)
for i in range(n+2):
    arr.append(i)
print(check,arr)
root = sqrt(n)
i = 2
k = 1
while i<=root:
    print("i:",i)
    if check[i]:
        arr[i]=k
        print("check ok")
        for j in range(i*i,n+2,i):
            print("j:",j)
            if check[j]:
                arr[j] = k
                check[j] = False
    k += 1
    i += 1
print(arr)

