# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 0

        def dfs(node, max_path_val):
            nonlocal num_good
            if not node: return

            if node.val >= max_path_val:
                num_good += 1
            
            max_path_val = max(node.val, max_path_val)

            dfs(node.left, max_path_val)
            dfs(node.right, max_path_val)
        
        dfs(root, root.val)
        return num_good
