tests = int(input(""))
while(tests>0):
    tests -= 1
    x,y,z = map(int, input().split())
    if x+z>=10:
        print("YES")
    elif y+x>=10:
        print("YES")
    elif y+z>=10:
        print("YES")
    else:
        print("NO")