#from sys import stdin
from collections import Counter
#input = stdin.readline
def solve(n,s):
    left,right = set(),Counter(s)
    Max = 0
    for i in s:
        right[i] -= 1
        if right[i]==0:
            right.pop(i)
        left.add(i)
        #print(left,right)
        Max = max(Max,len(left)+len(right))
    return Max

for i in range(int(input())):
    #arr = list(map(int,input().split()))
    n = int(input())
    s = input()
    #a,b = map(int,input().split())
    print(solve(n,s))
