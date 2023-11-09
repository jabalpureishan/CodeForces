n,x = map(int,input().split())

a,b = map(int,input().split())
set_ = set()
if a>b:
    set_.update(range(b,a+1))
else:
    set_.update(range(a,b+1))

for i in range(n-1):
    a,b = map(int,input().split())
    if a>b:
        set_.intersection_update(range(b,a+1))
    else:
        set_.intersection_update(range(a,b+1))
if len(set_)==0:
    print(-1)
else:
    if x in set_:
        print(0)
    else:
        print(min(abs(x-min(set_)),abs(x-max(set_))))
