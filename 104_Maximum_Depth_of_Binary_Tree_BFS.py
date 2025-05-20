# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        length=0
        q = []
        q.append(root)
        while q:
            for i in range(len(q)):
                item=q.pop(0)
                if item.left:
                    q.append(item.left)
                if item.right:
                    q.append(item.right)
            
            length+=1
        return length
        
