from collections import Counter
def solve(n,s):
    s = Counter(s)
    Max = max(s.items(),key=lambda x:x[1])
    return max(n%2,n-(n-Max[1])*2)







tests = int(input())
for i in range(tests):

    n = int(input())
    s = input()

    print(solve(n,s))
