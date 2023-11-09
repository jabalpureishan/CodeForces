tests = int(input(""))
for i in range(tests):
    length = int(input(""))
    arr = list(map(int, input().split()))
    ind = arr.index(min(arr))
    arr[ind] += 1
    prod = 1
    for i in arr:
        prod *= i 
    print(prod)