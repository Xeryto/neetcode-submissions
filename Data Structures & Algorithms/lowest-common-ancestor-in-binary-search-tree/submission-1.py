# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def bfs(root):
            p_parents = []
            q_parents = []

            que = [(root, [])]
            while que:
                node, parents = que.pop(0)
                parents.append(node)
                if node.val == p.val:
                    p_parents = parents[:]
                if node.val == q.val:
                    q_parents = parents[:]

                if node.left != None:
                    que.append((node.left, parents[:]))
                
                if node.right != None:
                    que.append((node.right, parents[:]))

            return (p_parents, q_parents)
        
        p_parents, q_parents = bfs(root)
        
        if len(p_parents) > len(q_parents):
            p_parents, q_parents = q_parents, p_parents
        
        while len(q_parents) > len(p_parents):
            q_parents.pop(-1)
        
        while True:
            q_node, p_node = q_parents.pop(-1), p_parents.pop(-1)

            if q_node == p_node:
                return q_node
        
        return root
