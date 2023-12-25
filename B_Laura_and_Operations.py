tests = int(input())
for i in range(tests):
    a,b,c = map(int,input().split())
    ans = []
    avg = b+c
    if avg%2!=0:
        print(0,end=" ")
    else:
        avg = avg//2
        if a>(avg-min(b,c)):
            print(1,end=" ")
        else:
            print(0,end=" ")
    avg = a+c
    if avg%2!=0:
        print(0,end=" ")
    else:
        avg = avg//2
        if b>(avg-min(a,c)):
            print(1,end=" ")
        else:
            print(0,end=" ")

    avg = b+a
    if avg%2!=0:
        print(0,end=" ")
    else:
        avg = avg//2
        if c>(avg-min(b,a)):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()