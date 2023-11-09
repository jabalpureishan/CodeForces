
def get_sum(num):
    ans = 0
    while num>0:
        ans += num%10
        num //= 10
    return ans
from math import floor,log10
num = int(input())
if num in range(0,10):
    print(0)
else:
    count = 0
    while floor(log10(num)+1)>1:
        num = get_sum(num)
        count += 1
    print(count)
