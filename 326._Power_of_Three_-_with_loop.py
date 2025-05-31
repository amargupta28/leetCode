class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=1
        while True:
            if i == n:
                return True
            elif i >n:
                return False
            i*=3
        
        
