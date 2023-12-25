from sys import stdin
input = stdin.readline

for i in range(int(input())):
    n  = int(input())
    arr = sorted(list(map(int,input().split())),reverse=True)
    neg = []
    pos = []
    for i in arr:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    Max = max(arr[0]*arr[1],arr[-1]*arr[-2])
    print(Max)