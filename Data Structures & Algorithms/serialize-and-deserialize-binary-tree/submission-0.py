# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        
        left, right = self.serialize(root.left), self.serialize(root.right)
        ans = str(root.val)+","+str(left)+","+str(right)
        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pre = data.split(",")
        idx = 0
        def dfs():
            nonlocal idx
            if pre[idx] == 'null':
                idx+=1
                return None
            node = TreeNode(pre[idx])
            idx+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))