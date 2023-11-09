#include <iostream>
#include <string>

using namespace std;

int main() {
    int tests;
    cin >> tests;

    for (int t = 0; t < tests; ++t) {
        int length, window;
        cin >> length >> window;
        int count = 0;
        string str;
        cin >> str;
        int var,var2;
        for (int i = 0; i < length; ++i) {
            if (str[i] == 'B') {
                var++;
            }
        }
        for (int i = 0; i < length; ++i) {
            if (str[i] == 'B') {
                var2++;
            }
        }
        for (int i = 0; i < length; ++i) {
            if (str[i] == 'B') {
                count++;
                i += window - 1;
            }
        }

        cout << count << endl;
    }

    return 0;
}
/*
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
    print(count)"""*/