
def sum_attached_nodes(target):
    parent = target // 2
    return target + parent * (target - 2**(len(bin(target))-3) + 1)
tests = int(input(""))
for i in range(tests):
    target  = int(input(""))
    #print(sum_attached_nodes(target))
    ans = 0
    while(target!=1):
        ans+=target
        target/=2
    print(target)
    
