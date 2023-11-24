from math import ceil
tests = int(input())
for i in range(tests):
    num = int(input())
    ans = 1
    while num>0:
        print(ans,end=" ")
        ans += 2
        num -=1
    print()