

tests = int(input(""))
for i in range(tests):
    n = int(input(""))
    array = tuple(map(int, input().split()))
    new = sorted(array)
    for i in range(n):
        if (array[i]%2==0)!=(new[i]%2==0) :
            print("NO")
            break
    else:
        print("YES")