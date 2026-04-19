# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isLeaf(node):
            return node.left is None and node.right is None
        
        def postorder(node):
            if not node:
                return None
            
            node.left = postorder(node.left)
            node.right = postorder(node.right)
            
            node = None if isLeaf(node) and node.val == target else node
            
            return node
        
        root = postorder(root)
        return root

'''
                     1
            2  <-            3
        5       N      2       5


            3
                3
            3
'''

            
        
        