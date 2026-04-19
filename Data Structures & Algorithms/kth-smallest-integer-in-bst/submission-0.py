# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        idx = 0
        while True:
            # Keep going left to prioritize the left
            while root:
                stack.append(root)
                root = root.left

            # Once there aren't any left values, get most recently added from stack
            root = stack.pop()
            idx += 1

            if idx == k: return root.val

            # Prioritize the right
            root = root.right