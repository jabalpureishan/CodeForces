d = {}
for i in range(0,10):
    d[(0,i)] = 1
    d[(i,0)] = 1
    d[(9,i)] = 1
    d[(i,9)] = 1
for i in range(1,9):
    d[(1,i)] = 2
    d[(i,1)] = 2
    d[(8,i)] = 2
    d[(i,8)] = 2
for i in range(2,8):
    d[(2,i)] = 3
    d[(i,2)] = 3
    d[(7,i)] = 3
    d[(i,7)] = 3
for i in range(3,7):
    d[(3,i)] = 4
    d[(i,3)] = 4
    d[(6,i)] = 4
    d[(i,6)] = 4
for i in range(4,6):
    d[(4,i)] = 5
    d[(i,4)] = 5
    d[(5,i)] = 5
    d[(i,5)] = 5
#print(d)

tests = int(input(""))
for i in range(tests):
    score = 0
    for j in range(10):
        string = input("")
        for k in range(10):
            if string[k]=="X":
                score += d[(j,k)]
    print(score)



