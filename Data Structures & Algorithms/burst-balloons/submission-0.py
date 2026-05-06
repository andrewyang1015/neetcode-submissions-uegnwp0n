class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)] # DP[i][j] = max coins from bursting subarray [i, j]

        for left in range(n, 0, -1):
            for right in range(left, n + 1):
                # At each subarray, need to check to see which baloon is the last to burst
                for burst in range(left, right + 1):
                    single_burst = nums[left - 1] * nums[burst] * nums[right + 1]
                    # Then solve the sub problems
                    total_collected = dp[left][burst - 1] + single_burst + dp[burst + 1][right]

                    dp[left][right] = max(dp[left][right], total_collected)
        
        # want the total problem space from 1 to n + 1
        return dp[1][n]

