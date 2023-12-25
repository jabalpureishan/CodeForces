from collections import Counter
def solve(n,s):
    count = 0
    s = Counter(s)
    for i in s:
        if s[i]>=ord(i)-64:
            count += 1
    return count



for i in range(int(input())):
    #arr = list(map(int,input().split()))
    n = int(input())
    s = input()
    # a,b = map(int,input().split())
    print(solve(n,s))
