class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        for num in range(n + 1):
            perfect_sq = 1
            res = num
            while num - perfect_sq**2 >= 0:
                res = min(res, 1 + dp[num - perfect_sq**2])
                perfect_sq += 1
            
            dp[num] = res
        
        return dp[n]
                