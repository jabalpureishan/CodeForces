d = {4:0,7:0,-1:1}
string = input()
for i in string:
    if i=="4":
        d[4] += 1
    elif i=="7":
        d[7] += 1
print(max(4,7,-1,key=lambda x:d[x]))