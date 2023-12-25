from sys import stdin
input = stdin.readline
def solve(l,r,k,pref):
    odds = pref[-1] - pref[r] - pref[l-1]
    if k%2!=0:
        odds += r-l+1
    if odds%2!=0:
        return "YES"
    return "NO" 




for i in range(int(input())):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    pref = [0]
    for i in arr:
        if i%2!=0:
            pref.append(pref[-1]+1)
        else:
            pref.append(pref[-1])
    for i in range(q):
        l,r,k = map(int,input().split())
        print(solve(l,r,k,pref))

