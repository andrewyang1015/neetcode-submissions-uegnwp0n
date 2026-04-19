# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Should store each node and the max profit from robbing and max profix if don't rob
        dp = {}

        def dfs(node):
            if not node:
                return 0
            
            if node in dp:
                return dp[node]
            
            # Max profit from robbing
            rob = node.val
            if node.left:
                rob += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob += dfs(node.right.left) + dfs(node.right.right)

            dont_rob = dfs(node.left) + dfs(node.right)

            dp[node] = max(rob, dont_rob)

            return dp[node]
        
        return dfs(root)