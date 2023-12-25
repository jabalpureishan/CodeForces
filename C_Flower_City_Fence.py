tests = int(input())
for i in range(tests):
    length = int(input())
    arr = list(map(int,input().split()))
    arr.append(0)
    ans = []
    curr = arr[0]
    ind = 0
    for j in range(length+1,0,-1):

        while ind<length and arr[ind]>=j:

            ind += 1
        #print("ind:",ind,"arr[j]",arr[j])
        ans.append(ind)
    ans = ans[::-1][:length]
    if ans==arr[:-1]:
        print("YES")
    else:
        print("NO")