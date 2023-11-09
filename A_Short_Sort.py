tests = int(input(""))
for i in range(tests):
    st = input("")
    string = []
    for i in st:
        string.append(i)
    one = string.copy()
    two = string.copy()
    three = string.copy()
    one[0],one[2] = one[2],one[0]
    two[1],two[2] = two[2],two[1]
    three[0],three[1] = three[1],three[0]
    #print(one,two,three)
    ans = ["a","b","c"]
    if one==ans or two==ans or three==ans or string==ans:
        print("YES")
    else:
        print("NO")