from math import sqrt
def calculate(paintings,cardboard,array):
    a = 4*paintings
    b = c = 0
    for i in array:
        b += 4*i
        c += i*i
    c = c - cardboard
    #print(a,b,c)
    dis = b * b - 4 * a * c
    sqrt_val = sqrt(abs(dis))
    if dis>0:
        first = (-b + sqrt_val)/(2 * a)
        second = (-b - sqrt_val)/(2 * a)
        first,second = int(first),int(second)
        return max(first,second)
    elif dis==0:
        ans = -b / (2 * a)
        ans = int(ans)
        return abs(ans)

tests = int(input(""))
while(tests>0):
    tests -= 1
    paintings,cardboard = map(int, input().split())
    array = tuple(map(int, input().split()))
    #print("ans:")
    print(calculate(paintings,cardboard,array))