import sys
input = sys.stdin.readline
for i in range(int(input())):
    count = 0
    for j in range(int(input())):
        a,b = map(int,input().split())
        if a>b:
            count += 1
    print(count)
