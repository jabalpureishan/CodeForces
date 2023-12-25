







tests = int(input())
for i in range(tests):
    # arr = list(map(int,input().split()))
    # intvar = int(input())
    s = input()
    # multi,var = map(int,input().split())
    letters = "abcdefgh"
    nums = "12345678"
    for i in nums:
        curr = s[0]+i
        if curr!=s:
            print(curr)
    for i in letters:
        curr = i+s[1]
        if curr!=s:
            print(curr)
