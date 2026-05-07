class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)

        def backtrack(idx, curVal):
            if idx == n: 
                return 1 if curVal == target else 0

            if (idx, curVal) in dp: return dp[(idx, curVal)]

            include_add = backtrack(idx + 1, curVal + nums[idx])
            include_sub = backtrack(idx + 1, curVal - nums[idx])

            dp[(idx, curVal)] = include_add + include_sub

            return dp[(idx, curVal)]

        return backtrack(0, 0)


