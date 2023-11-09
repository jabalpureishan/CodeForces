from collections import deque
length,rot = map(int,input().split())
string = input()
arr = []
for i in string:
    arr.append(i)
if length==1:
    print(string)
else:
    for i in range(rot):
        j = 0
        while j+1<length:
            if arr[j]=="B" and arr[j+1]=="G":
                arr[j],arr[j+1]=arr[j+1],arr[j]
                j += 1
            j += 1
    print("".join(arr))