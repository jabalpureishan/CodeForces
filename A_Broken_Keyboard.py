# def solve(s):
#     n,broken = len(s),set()
#     if n==1:
#         return s
#     ind = 0
#     while ind+1<n:
#         if s[ind]!=s[ind+1]:
#             broken.add(s[ind])
#         else:
#             ind += 1
#         ind += 1
#     if s[-1]!=s[-2]:
#         broken.add(s[-1])
#     return "".join(sorted(broken))













# tests = int(input())
# for i in range(tests):
#     # arr = list(map(int,input().split()))
#     # intvar = int(input())
#     s = input()
#     # multi,var = map(int,input().split())
#     print(solve(s))

print(3%3)