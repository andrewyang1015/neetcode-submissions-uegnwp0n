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

        visited = None # Tracks last processed node
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            # Move to the right if found right child
            node = stack[-1]
            if node.right and node.right != visited: 
                node = node.right
                continue

            # Otherwise is leaf node
            stack.pop()
            if isLeaf(node) and node.val == target:
                if not stack: return None

                # Update parent references
                parent = stack[-1]
                if parent.left == node:
                    parent.left = None
                elif parent.right == node:
                    parent.right = None
            else:
                visited = node
            node = None
        return root
            
            

'''
                     1
            2  <-            3
        5       N      2       5


            3 <
                3 <
            3 <
                <
3


[3, 3]

3 -> yes leaf
'''
            
