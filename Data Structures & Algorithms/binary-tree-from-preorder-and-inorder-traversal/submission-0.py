# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inor = {}
        for i,val in enumerate(inorder):
            inor[val] = i
        
        
        # index = inor[preorder[0]]
        
        def dfs(pre, start, end):
            if not pre:
                return None
            
            index = inor[pre[0]]
            if index < start or index > end:
                return None

            val = pre.pop(0)
            node = TreeNode(val)
            
            node.left = dfs(pre, start, index)
            node.right = dfs(pre, index, end)
            return node
        
        return dfs(preorder, 0, len(inorder))


