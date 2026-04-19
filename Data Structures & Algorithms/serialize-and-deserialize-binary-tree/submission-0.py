# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if not node:
                return ["None"]
            
            value = str(node.val)
            left = preorder(node.left)
            right = preorder(node.right)

            return [value] + left + right
        
        return  ",".join(preorder(root))
        
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(",")
        preorder_idx = 0

        def dfs():
            nonlocal preorder_idx
            if preorder[preorder_idx] == 'None':
                preorder_idx += 1
                return None
            
            node = TreeNode(int(preorder[preorder_idx]))
            preorder_idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
