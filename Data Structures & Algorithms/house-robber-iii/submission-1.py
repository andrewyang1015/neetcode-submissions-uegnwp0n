# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        dp = {}

        stack = []
        visited = None
        node = root

        # ------------ BOILERPLATE_START ----------------
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack[-1]
            if node.right and node.right != visited:
                node = node.right
                continue
            
            stack.pop()
        # ------------ BOILERPLATE_END ----------------

            # Special processing
            left_subtree = dp[node.left] if node.left else 0
            right_subtree = dp[node.right] if node.right else 0
            left_left_subtree, left_right_subtree, right_left_subtree, right_right_subtree = 0, 0, 0, 0

            if node.left:
                left_left_subtree = dp[node.left.left] if node.left.left else 0
                left_right_subtree = dp[node.left.right] if node.left.right else 0
            if node.right:
                right_left_subtree = dp[node.right.left] if node.right.left else 0
                right_right_subtree = dp[node.right.right] if node.right.right else 0
            
            dont_rob = left_subtree + right_subtree
            rob = node.val + left_left_subtree + left_right_subtree + right_left_subtree + right_right_subtree

            dp[node] = max(dont_rob, rob)

        # ------------ BOILERPLATE_START ----------------
            visited = node
            node = None
        # ------------ BOILERPLATE_END ----------------

        return dp[root]