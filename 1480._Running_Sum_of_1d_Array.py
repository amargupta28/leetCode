class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output=[]
        prev=0
        
        for i in nums:
            output.append(prev+i)
            prev=output[-1]
        return output
