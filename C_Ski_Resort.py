from sys import stdin
input = stdin.readline
def solve(n,days,temp,arr):
    arr.append(temp+1)
    prev,ans = 0,0
    for i in range(n+1):
        if arr[i]>temp:
            diff = max(0,i-prev-days+1)
            ans += (diff*(diff+1))//2
            prev = i+1
    return ans
        



for i in range(int(input())):
    
    n,days,temp = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(n,days,temp,arr))
