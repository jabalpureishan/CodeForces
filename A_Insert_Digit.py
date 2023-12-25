# from sys import stdin
# input = stdin.readline

def solve(n,b,s): 
    new = s[:]   
    n = int(n)
    ind = n-1
    c = int(b)
    # while ind>-1 and int(s[ind])<c :
    #     #print(s[ind])
    #     ind -= 1
    # if ind==n-1:
    #     s = s+b
    # elif ind==-1:
    #     s = b+s
    # else:
    #     s = s[:ind]+b+s[ind:]
    ind = 0
    #print("curr:",new[ind],c)
    while ind<n and c<int(new[ind]):
        #print("ind:",new[ind])
        ind += 1
    if ind==n:
        new += b
    elif ind==0:
        new = b+new
    else:
        new = new[:ind]+b+new[ind:]
    return new


for i in range(int(input())):
    n,b = map(str,input().split())
    s = input()
    print(solve(n,b,s))
    #print("-----------")

