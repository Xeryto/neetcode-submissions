# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0

    def dfs(self, root):
        if not root:
            return 0
        
        l,r = self.dfs(root.left),self.dfs(root.right)
        self.ans = max(l+r, self.ans)

        return 1+max(l,r)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans