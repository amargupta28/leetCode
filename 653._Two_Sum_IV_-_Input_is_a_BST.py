# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.arr=[]
        def inorder(root):
            if root:
                inorder(root.left)
                self.arr.append(root.val)
                inorder(root.right)
        inorder(root)
        print(self.arr)
        i=0
        j=len(self.arr)-1
        while i <j:
            if self.arr[i] +self.arr[j] == k:
                return True
            elif self.arr[i] +self.arr[j] < k:
                i+=1
            else:
                j-=1
        return False
