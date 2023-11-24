def solve(num):
    if num in {1,2}:
        return "First"
    if num%3==0:
        return "Second"
    return "First"

tests = int(input())
for i in range(tests):
    num = int(input())
    print(solve(num))
