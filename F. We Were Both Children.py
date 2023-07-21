tests = int(float(input("")))
for i in range(tests):
    length = int(input(""))
    array = tuple(map(int, input().split()))
    d = {}
    for i in range(length):
        
        jump = array[i]
        if jump>length:
            continue
        print("jump:",jump)
        pos = 0
        for j in range(length):
            print(pos,end=" ")
            d[pos] = d.get(pos,0) + 1
            pos += jump
        print()
    if 0 in d:
        d.pop(0)
    print("d:",d)
    print("ans:")
    if len(d)==0:
        print(0)
    else:
        print(max(d.values()))
