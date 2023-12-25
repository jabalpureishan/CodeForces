from sys import stdin
input = stdin.readline
def solve(n,arr1,arr2,arr3):
    d1,d2,d3 = {},{},{}
    for i in range(n):
        d1[i] = arr1[i]
        d2[i] = arr2[i]
        d3[i] = arr3[i]
    d1 = sorted(d1.items(),key=lambda x:x[1],reverse=True)    
    d2 = sorted(d2.items(),key=lambda x:x[1],reverse=True)
    d3 = sorted(d3.items(),key=lambda x:x[1],reverse=True)    
    p1 = p2 = p3 = 0
    print(d1)
    print(d2)
    print(d3)
    return ""
    while (d1[p1][0]==d2[p2][0] or d1[p1][0]==d3[p3][0] or d2[p2][0]==d3[p3][0]) and (p1<n and p2<n and p3<n):
        print(d1[p1][0],d2[p2][0],d3[p3][0])
        if d1[p1][0]==d2[p2][0]:
            if d1[p1+1][1]>=d2[p2+1][1]:
                p1 += 1
            else:
                p2 += 1
        if d1[p1][0]==d3[p2][0]:
            if d1[p1+1][1]>=d3[p3+1][1]:
                p1 += 1
            else:
                p3 += 1
        if d3[p1][0]==d2[p2][0]:
            if d3[p3+1][1]>=d2[p2+1][1]:
                p3 += 1
            else:
                p2 += 1
    
    return d1[p1][1] + d2[p2][1] + d3[p1][1]

for i in range(int(input())):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    arr3 = list(map(int,input().split()))
    print(solve(n,arr1,arr2,arr3))
