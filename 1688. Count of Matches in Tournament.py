def solution(n):
    ans = 0
    while n>1:
        div = n//2
        ans += div
        n -= div
    return ans

print(solution(7))
print(solution(14))
