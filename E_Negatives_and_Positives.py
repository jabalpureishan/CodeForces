from sys import stdin
input = stdin.readline
def solve(arr,n):
    sum_ = sum(arr)
    for i in range(n-1):
        add = -arr[i]-arr[i+1]   
        sub = arr[i]+arr[i+1]
        temp = sum_ + add - sub
        print(add,sub,temp,sum_)
        if temp>sum_:
            sum_ = temp
            arr[i] = -arr[i]
            arr[i+1] = -arr[i+1]
         
    return sum_


for i in range(int(input())):
    
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(arr,n))
    print("------------")
