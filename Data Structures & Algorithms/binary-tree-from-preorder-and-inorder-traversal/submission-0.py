# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx = 0
        inorder_mapping = defaultdict(int)
        n = len(preorder)

        for i, val in enumerate(inorder):
            inorder_mapping[val] = i

        def dfs(left, right):
            nonlocal preorder_idx
            if left > right:
                return None

            node = TreeNode(preorder[preorder_idx])
            preorder_idx += 1
            
            inorder_idx = inorder_mapping[node.val]

            node.left = dfs(left, inorder_idx - 1)
            node.right = dfs(inorder_idx + 1, right)
            return node

        
        return dfs(0, n - 1)