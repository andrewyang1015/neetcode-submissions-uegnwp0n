class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        tot_sum = sum(stones)
        mid = tot_sum // 2
        n = len(stones)

        # DP Tells us whether we can form the sum i from 0 to total/2 or not
        dp = [False] * (mid + 1)
        dp[0] = True

        for idx in range(n):
            for curSum in range(mid, idx -1, -1):
                if curSum - stones[idx] >= 0:
                    dp[curSum] = dp[curSum] or dp[curSum - stones[idx]]
        
        min_val = float("inf")

        # Then calculate what that split is
        for i, state in enumerate(dp):
            if state:
                min_val = min(min_val, abs(i - (tot_sum - i)))
        
        return min_val

'''

0
1
...
mid
'''