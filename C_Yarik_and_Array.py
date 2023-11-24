def maxSubArraySum(a, size):
    far = float("-inf")
    max_here = 0
 
    for i in range(0, size):
        max_here = max_here + a[i]
        if (far < max_here):
            far = max_here
 
        if max_here < 0:
            max_here = 0
    return far
def solve(arr,n):
    ind = []
    p1 = 1
    last = 0
    arr.append(arr[-1])
    while p1<n+1:
        #print("ch",arr[p1],arr[p1-1])
        if (arr[p1]%2==0 and arr[p1-1]%2==0) or (arr[p1]%2!=0 and arr[p1-1]%2!=0):
            #print("in")
            ind.append([last,p1-1])
            last = p1
        p1 += 1
    Max = float("-inf")
    for i in ind:
        Max = max(Max,maxSubArraySum(arr[i[0]:i[1]+1],len(arr[i[0]:i[1]+1])))
    return Max





tests = int(input())
for i in range(tests):
    n = int(input())
    arr = list(map(int,input().split()))
    
    # strvar = input()
    # multi,var = map(int,input().split())
    print(solve(arr,n))
