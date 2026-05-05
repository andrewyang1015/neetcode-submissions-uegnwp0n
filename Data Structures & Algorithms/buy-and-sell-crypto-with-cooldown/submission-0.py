class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)] # Selling or buying while include i in n

        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    dont_buy = dp[i + 1][0] # Have to continue looking at previous dont buys
                    buy = dp[i + 1][1] - prices[i] # Must have sold some point in the future
                    dp[i][0] = max(dont_buy, buy)
                else:
                    dont_sell = dp[i + 1][1]
                    sell = dp[i + 2][0] + prices[i] if i + 1 < n else prices[i]
                    dp[i][1] = max(dont_sell, sell)
        
        # Can't sell at the beginning so start with a buy
        return dp[0][0]


        
'''


'''