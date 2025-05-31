class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l1=[0]*(len(nums)+1)
        for i in nums:
            if i >0 and i <len(l1):
                l1[i] +=1
        print(l1)
        for i in range(1,len(l1)):
            if l1[i] == 0:
                return i
        return len(l1)
