class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3

        for i in range(4, n + 1):
            res = i
            # Try all possible splits from 2 up
            for split in range(2, i):
                res = max(res, dp[split] * dp[i - split])
            dp[i] = res
        
        return dp[n]

'''
            12
        6       6
    3       3 3    3

'''