tests = int(input(""))
while(tests>0):
    tests -= 1
    matrix = []
    for i in range(8):
        array = input("")
        matrix.append(array)
    word = ""
    for i in matrix:
        for j in i:
            if j.isalpha():
                word += j
    print(word)

