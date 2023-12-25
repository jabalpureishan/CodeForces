from sys import stdin
input = stdin.readline
def solve(n):
    a,b = 0,n-1
    arr = []
    while a<=b:
        if a==b:
            arr.append(a)
        else:
            arr.extend([a,b])
        a += 1
        b -= 1
    if arr[0]==0:
        arr[0] = n
    mark = n
    for i in range(1,n):
        #print("mark:",mark)
        curr = arr[i] + arr[i-1]
        #print("curr:",curr)
        if curr>=mark+n:
            mark += n
            #print("mark change to:",mark,curr)
        arr[i] += mark
    ans = [arr[0]]
    for i in range(1,n):
        ans.append(arr[i]-arr[i-1])
        if ans[i]==ans[i-1]:
            return [-1]

    return ans



for i in range(int(input())):
    # arr = list(map(int,input().split()))
    n = int(input())
    # s = input()
    # a,b = map(int,input().split())
    res = solve(n)
    for i in res:
        print(i,end=" ")
    print()
    #print("--------------------")
