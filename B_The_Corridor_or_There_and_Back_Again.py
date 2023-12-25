

tests = int(input())
for i in range(tests):
    length = int(input())
    Min = float("inf")
    for j in range(length):
        d,s = map(int,input().split())
        Min = min(Min,d+(s-1)//2)
    print(Min)