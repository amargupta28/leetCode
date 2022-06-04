# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[]
        queue.append(root)
        result=[]
        while queue:
            temp=[]
            res=[]
            while queue:
                temp.append(queue.pop(0))
                res.append(temp[-1].val)
            result.append(res)
            while temp:
                tem= temp.pop(0)
                if tem.left:
                    queue.append(tem.left)
                if tem.right:
                    queue.append(tem.right)
        return (result)
