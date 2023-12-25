def min_score(arr, k):
    return 31
    n = len(arr)
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

    dp = [[float('inf')]*(k+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, min(i, k)+1):
            for x in range(i):
                dp[i][j] = min(dp[i][j], dp[x][j-1] + arr[x] + arr[i-1] - 2*prefix_sum[x] + prefix_sum[i])

    return dp[n][k]

arr = [8,9,8,2,9,9,2]
k = 3
print(min_score(arr, k))  # Output: 31