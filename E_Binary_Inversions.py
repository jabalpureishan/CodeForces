from sys import stdin
input = stdin.readline
def solve(arr,n):
    score = 0
    ones = zeroes = 0
    for i in range(n-1,-1,-1):
        if arr[i]==1:
            score += zeroes
        else:
            zeroes += 1
    Max = score
    ones = 0
    for i in arr:
        if i==1:
            Max = max(Max,score+ones-zeroes)
            ones += 1
        else:
            zeroes -= 1
            Max = max(Max,score-ones+zeroes)
    return Max
    #leftones = rightzeroe






for i in range(int(input())):
    
    n = int(input())
    #s = input()
    #a,b = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solve(arr,n))
