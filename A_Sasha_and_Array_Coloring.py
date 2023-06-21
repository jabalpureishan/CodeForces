tests = int(input(""))
for i in range(tests):
    length = int(input(""))
    array  = list(map(int, input().split()))
    array.sort()
    #print("array:",array)
    if length%2==0:
        loop = length//2
    else:
        loop = (length-1)//2
    #print("loop:",loop)
    total = 0
    for i in range(loop):
        total += array[-(i+1)] - array[i]
    print(total)