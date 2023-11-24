from collections import Counter
def solve(n,k,s):
    d = Counter(s)
    odd = 0
    for i in d:
        if d[i]%2!=0:
            odd += 1
    if k<odd-1:
        return "NO"
    return "YES"
    












tests = int(input())
for i in range(tests):    
    n,k = map(int,input().split())
    s = input()
    print(solve(n,k,s))
