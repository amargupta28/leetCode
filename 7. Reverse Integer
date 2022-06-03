class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverseArray= "0"
        nums=abs(x)
        while nums >0:
            reverseArray+= str(nums%10)
            nums=nums//10
        
        reverseArray= int(reverseArray)
        if reverseArray <=(-2**31) or reverseArray >= ((2**31) -1) :
            return 0
        if x <0:
            return -reverseArray
        else:
            return reverseArray
            
