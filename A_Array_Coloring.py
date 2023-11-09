from sys import stdin
input = stdin.readline
def solve(array,length):
    odd,even = 0,0
    for i in array:
        if i&1==0:
            even += 1
        else:
            odd += 1
    if odd&1==1:
        return "NO"
    return "YES"



test = int(input())
for i in range(test):
    length = int(input())
    array = tuple(map(int,input().split()))
    print(solve(array,length))