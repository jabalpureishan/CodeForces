def solution(arr,k):
    if k in {2,3,5}:
        Min = float("inf")
        for i in arr:
            if i%k==0:
                return 0
            div = i//k
            Min = min(Min,k*(div+1)-i)
        return Min
    else:
        even = 0
        for i in arr:
            if i%k==0:
                return 0
            if i%2==0:
                even += 1
        Min = float("inf")
        for i in arr:
            if i%k==0:
                return 0
            div = i//k
            Min = min(Min,k*(div+1)-i)
        return min(Min,max(0,2-even))
            



tests = int(input())
for i in range(tests):
    length,k = map(int,input().split())
    arr = list(map(int,input().split()))
    print(solution(arr,k))