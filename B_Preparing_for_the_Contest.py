
def solve(a,b):
    if b==0:
        for i in range(a,0,-1):
            print(i,end=" ")
    elif a==b:
        for i in range(1,a+1):
            print(i,end=" ")
    else:
        print(1,end=" ")
        for i in range(2,1+b):
            print(i,end=" ")
        for i in range(a,b,-1):
            print(i,end=" ")
    return ""


for i in range(int(input())):
    # arr = list(map(int,input().split()))
    # n = int(input())
    # s = input()
    a,b = map(int,input().split())
    print(solve(a,b))
