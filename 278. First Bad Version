# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left < right:
            midpt= (left+right)//2
            if isBadVersion(midpt):
                right = midpt
            else:
                left= midpt+1
        return left
