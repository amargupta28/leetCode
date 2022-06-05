class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <2:
            return x
        left =2
        right= x//2
        while left <= right:
            pivot= (left+right)//2
            
            temp = pivot*pivot
            if temp > x:
                right = pivot-1
            elif temp<x:
                left = pivot+1
            else:
                return pivot
        return right
