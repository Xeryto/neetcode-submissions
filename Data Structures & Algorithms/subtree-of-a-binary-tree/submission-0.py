# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(node):
            pre = []
            if not node:
                pre.append(node)
            else:
                pre.extend(preorder(node.left))
                pre.extend(preorder(node.right))
                pre.append(node.val)
            
            return pre
        
        r, sr = preorder(root), preorder(subRoot)
        if len(sr) >= len(r):
            return sr == r

        left,right = 0, len(sr)-1
        while right < len(r):
            if r[left:right+1] == sr:
                return True
            right+=1
            left+=1
        return False
             

        