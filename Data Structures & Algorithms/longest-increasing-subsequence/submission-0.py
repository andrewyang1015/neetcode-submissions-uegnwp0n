import bisect
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                idx_to_replace = bisect.bisect_left(dp, nums[i])
                dp[idx_to_replace] = nums[i]
        return len(dp)
        
        