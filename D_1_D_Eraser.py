tests = int(input(""))
for i in range(tests):
    length,window = input().split()
    length,window = int(length),int(window)
    count = 0
    string = input("")
    for i in range(length):
        if string[i]=="B":
            count += 1
            i += window - 1
    print(count)
    """
    B = string[:window].count("B")
    d = {(0,window-1):B}
    slides = length - window
    for j in range(slides):
        if string[window]=="B":
            B += 1
        if string[j]=="B":
            B -= 1
        window += 1
        d[(j+1,window-1)]=B
    d = sorted(d.items(),reverse=True,key=lambda x:x[1])
    #print(d)
    ind = 0
    changed = set()
    while(string.count("B")!=0):
        if d[ind][0][1] not in changed and d[ind][0][0] not in changed:
            leng = d[ind][0][1]+1 - d[ind][0][0]
            part = string[d[ind][0][0]:d[ind][0][1]+1]
            corr = "W"*leng
            if part!=corr:
                count += 1
                string = string[:d[ind][0][0]] + corr + string[d[ind][0][1]+1:]
                changed.add(d[ind][0][0])
                changed.add(d[ind][0][1])
            #print(string)
        #print("*")
        ind += 1
    print(count)"""


