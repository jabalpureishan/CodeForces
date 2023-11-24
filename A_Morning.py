str = "1234567890"
d = {}
for i in range(10):
    d[str[i]] = i
def solve(s):
    s = "1"+s
    lens = len(s)
    count = 0
    for i in range(1,lens):
        count += abs(d[s[i]]-d[s[i-1]])+1
    return count

tests = int(input())
for i in range(tests):
    s = input()
    print(solve(s))
