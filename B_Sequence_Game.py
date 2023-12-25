cases = int(input())
for i in range(cases):
    length = int(input())
    array = list(map(int,input().split()))
    ans = [array[0]]
    for j in range(1,length):
        if array[j]<array[j-1]:
            ans.append(1)
        ans.append(array[j])
    print(len(ans))
    for j in ans:
        print(j,end=" ")
    print()
