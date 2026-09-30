# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(p,q):
            p_que = [p]
            q_que = [q]

            while p_que and q_que:
                curp, curq = p_que.pop(0), q_que.pop(0)
                if not curp or not curq:
                    if curp != curq:
                        return False
                    continue
                if not (curp.val == curq.val):
                    return False
                p_que.append(curp.left)
                q_que.append(curq.left)
                p_que.append(curp.right)
                q_que.append(curq.right)
            
            return len(p_que)+len(q_que) == 0
        
        return bfs(p,q)