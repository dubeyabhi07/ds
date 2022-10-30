def solve(nums, X):
    N = len(nums)
    minn = min(nums)
    for i in range(len(nums)):
        nums[i] -= minn
    maxn = max(nums) + 1 
    dp = [[float('inf')]*(maxn) for _ in range(N)]

    # Initialize base case
    for j in range(maxn):
        dp[0][j] = abs(nums[0]-j)
    
    for i in range(1, len(nums)):
        min_so_far = min(dp[i-1][:i])
        for j in range(i, maxn): # starting from i to ensure strictly increasing order
            dp[i][j] = abs(nums[i]-j) + min_so_far
            min_so_far = min(min_so_far, dp[i-1][j])
    return "YES " + str(min(dp[-1])) if min(dp[-1]) <= X else "NO"
