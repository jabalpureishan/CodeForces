from sys import stdin
from math import sqrt
input = stdin.readline
def div(n):
    ans = []
    root = sqrt(n)
    i = 2
    while i<=root:
        if n%i==0:
            ans.append(i)
        i += 1
    while i>1:
        if n%i==0 and n//i!=i:
            ans.append(n//i)
        i -= 1

    return ans

def solve(num):
    d = div(num)
    
    n = len(d)
    for j in range(n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                if d[j]*d[k]*d[l]==num:
                    return "YES"+"\n"+str(d[j])+" "+str(d[k])+" "+str(d[l])
    return "NO"


for i in range(int(input())):
    print(solve(int(input())))

