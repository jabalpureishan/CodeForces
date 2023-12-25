tests = int(input())
string = "vika"
for i in range(tests):
    n,m = map(int,input().split())
    arr = []
    for j in range(m):
        arr.append(set())
    for j in range(n):
        curr = input()
        for k in range(m):
            #print("curr[k]:",curr[k])
            arr[k].add(curr[k])
    #print(arr)
    p1,p2 = 0,0
    while p1<4 and p2<m:
        #print(string[p1],arr[p2])
        if string[p1] in arr[p2]:
            p1 += 1
        p2 += 1
    if p1==4:
        print("YES")
    else:
        print("NO")
    


