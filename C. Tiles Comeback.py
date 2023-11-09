
def run(n,k,array):
    first,last,fcount,lcount = array[0],array[-1],0,0
    if first==last:
        occur = array.count(first)
        Sum = first*2
        for i in range(occur//2):
            if Sum%k==0 and ((i+1)*2)%k==0:
                return "YES"
            Sum += first*2
        return "NO"
    else:
        for i in range(n):
            if array[i]==first:
                fcount += 1
            elif array[i]==last:
                break
        for i in range(-1,-(n+1),-1):
            if array[i]==last:
                lcount += 1
            elif array[i]==first:
                break     
        Sum = first + last   
        for i in range(min(fcount,lcount)): 
            if Sum%k==0 and ((i+1)*2)%k==0:
                return "YES"
            Sum += first + last  
        return "NO" 



tests = int((input("")))
for i in range(tests):
    n,k = map(int, input("").split())
    array = tuple(map(int, input("").split()))
    print(run(n,k,array))