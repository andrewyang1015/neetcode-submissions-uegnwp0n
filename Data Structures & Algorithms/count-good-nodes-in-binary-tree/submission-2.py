# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_path_val):
            if not node: return 0

            good = 1 if node.val >= max_path_val else 0
            
            max_path_val = max(node.val, max_path_val)

            return dfs(node.left, max_path_val) + dfs(node.right, max_path_val) + good
        
        return dfs(root, root.val)
