from collections import Counter
length = int(input())
arr = set(map(int,input().split()))
ans = 0
for i in range(1,length+1):
    if i not in arr:
        ans += 1
print(ans)