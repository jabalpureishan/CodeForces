def solve(s):
    length = len(s)
    upper = []
    lower = []
    for i in range(length):
        #print("curr:",s[i])
        if s[i]=="B":
            s[i] = ""
            if len(upper)>=1:
                s[upper.pop()]=""
        elif s[i]=="b":
            s[i] = ""
            if len(lower)>=1:
                s[lower.pop()]=""
        else:
            if s[i].isupper():
                upper.append(i)
            else:
                lower.append(i)    
    return "".join(s)
 
 
 
 
 
tests = int(input())
for i in range(tests):
    # arr = list(map(int,input().split()))
    # intvar = int(input())
    s = list(input())
    # multi,var = map(int,input().split())
    print(solve(s))