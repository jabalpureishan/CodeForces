#include <iostream>
#include <vector>
using namespace std;

int solve(vector<int>& arr, int n) {
    vector<int> ans(n + 1, 0);
    int Max = 0;

    for (int i : arr) {
        for (int j = i; j <= n; j += i) {
            ans[j]++;
            Max = max(Max, ans[j]);
        }
    }

    return Max;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<int> arr(n);

        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        cout << solve(arr, n) << endl;
    }

    return 0;
}
