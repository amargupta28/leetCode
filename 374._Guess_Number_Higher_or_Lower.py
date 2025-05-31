# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left =1
        right=n
        
        while left <= right:
            midpt= (left+right)//2
            
            if guess(midpt) == 0:
                return midpt
            elif guess(midpt) == -1:
                right = midpt-1
            else:
                left= midpt+1
        
