# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        queue = deque([(root, root.val)])

        while queue:
            node, max_path_val = queue.popleft()

            if node.val >= max_path_val: good += 1

            max_path_val = max(max_path_val, node.val)

            if node.left: queue.append((node.left, max_path_val))

            if node.right: queue.append((node.right, max_path_val))
        
        return good
