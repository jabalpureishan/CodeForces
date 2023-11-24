from math import ceil
def solve(a,b,c):
    return ceil((abs(a-b)/2)/c)













tests = int(input())
for i in range(tests):
    # arr = list(map(int,input().split()))
    # intvar = int(input())
    # strvar = input()
    a,b,c = map(int,input().split())
    print(solve(a,b,c))
