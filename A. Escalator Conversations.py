tests = int(input(""))
for i in range(tests):
    n,m,k,H = map(int, input().split())
    array = tuple(map(int, input().split()))
    Set = set()
    for i in range(1,m):
        Set.add(i*k)
    count = 0
    for i in array:
        sub = abs(H-i)
        if sub in Set:
            count += 1
    print(count)






