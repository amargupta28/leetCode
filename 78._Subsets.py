class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[[]]
        
        for i in nums:
            output+=[lst+[i] for lst in output]
        return output
