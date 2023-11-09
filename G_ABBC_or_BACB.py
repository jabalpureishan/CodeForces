tests = int(input(""))
while(tests>0):
    tests -= 1
    string = input("")
    string2 = string[:]
    length = len(string)
    slides = length - 1
    coins = 0
    while(True):
        window = 2
        for j in range(slides):
            if string[j:window]=="AB":
                string = string[:j] + "BC" + string[window:]
                coins += 1
                break
            if string[j:window]=="BA":
                string = string[:j] + "CB" + string[window:]
                coins += 1
                break
            window += 1
        else:
            break
    coins2 = 0
    while(True):
        window = 2
        for j in range(slides):
            if string2[j:window]=="BA":
                string2 = string2[:j] + "CB" + string2[window:]
                coins2 += 1
                break
            if string2[j:window]=="AB":
                string2 = string2[:j] + "BC" + string2[window:]
                coins2 += 1
                break

            window += 1
        else:
            break
    print(max(coins,coins2))

