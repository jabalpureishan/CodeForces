import math
def printDivisors(n) :
    i = 1
    ans = []
    while i <= math.sqrt(n):
        if (n % i == 0) :
            if (n / i == i) :
                ans.append(i)
            else :
                ans.extend([i,int(n/i)])
        i = i + 1
    return ans

def solve(n,b):
    prefix = []
    sum_ = 0
    for i in b:
        sum_ += i
        prefix.append(sum_)
    
    divisors = printDivisors(n)
    ans = 0
    for i in divisors:
        window = i
        slides = n//i
        Max,Min = float("-inf"),float("inf")
        f,t = 0,i
        for j in range(slides):
            curr = sum(b[f:t])
            f+= i
            t += i
            Max = max(Max,curr)
            Min = min(Min,curr)
            #print("curr:",curr)
        #print(Max-Min)
        ans = max(ans,Max-Min)
        
    return ans




tests = int(input())
for i in range(tests):
    n = int(input())
    b = list(map(int,input().split()))
    print(solve(n,b))

