tests = int(input(""))
while(tests>0):
    tests -= 1
    length = int(input(""))
    Arr = tuple(map(int, input("").split()))
    print(estimate_num_liars(length,Arr))


