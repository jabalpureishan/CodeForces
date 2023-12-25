from sys import stdin
input = stdin.readline

for i in range(int(input())):
    n,t = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    Max = ind = 0
    Maxind = -1
    while t>0 and ind<n:
        #print(t)
        if t>=a[ind] and b[ind]>Max:
            #print("ind")
            Max = b[ind]
            Maxind = ind+1
        t -= 1
        
        ind += 1
    print(Maxind)
    #print("---------------")
