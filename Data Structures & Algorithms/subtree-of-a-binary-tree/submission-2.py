# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root:
            return True
        elif not (subRoot and root):
            return False
        
        return self.checkNode(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def checkNode(self, root, subRoot):
        if not subRoot and not root:
            return True
        elif not (subRoot and root):
            return False
        
        if root.val == subRoot.val and self.checkNode(root.left, subRoot.left) and self.checkNode(root.right, subRoot.right):
            return True
        
        return False
    