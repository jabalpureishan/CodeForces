#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <climits>

using namespace std;

int solve(vector<int>& arr, int n) {
    if (n <= 3) {
        return 0;
    }

    sort(arr.begin(), arr.end());
    int Min = INT_MAX;

    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int arrlj = (arr[n - 1] + arr[min(n - 1, j + 1)]) / 2;
            int arrij = (arr[j] + arr[i + 1]) / 2;
            int arrsi = (arr[i] + arr[0]) / 2;

            Min = min(Min, max({abs(arr[n - 1] - arrlj), abs(arr[min(n - 1, j + 1)] - arrlj), abs(arr[j] - arrij), abs(arr[i + 1] - arrij), abs(arr[i] - arrsi), abs(arr[0] - arrsi)}));
        }
    }

    return ceil((double)Min);
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        vector<int> arr(n);

        for (int j = 0; j < n; j++) {
            cin >> arr[j];
        }

        cout << solve(arr, n) << endl;
    }

    return 0;
}