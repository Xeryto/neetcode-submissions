# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0)])
        ans = []
        cur = []
        curLvl = 0
        while q:
            node, level = q.popleft()
            if level != curLvl and len(ans) < curLvl+1:
                ans.append(cur)
                cur = []
                curLvl+=1
            cur.append(node.val)
            
            if node.left:
                q.append((node.left, level+1))
            
            if node.right:
                q.append((node.right, level+1))
        
        ans.append(cur)
        return ans
