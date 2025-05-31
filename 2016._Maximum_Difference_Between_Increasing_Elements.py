class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxD = -1
        i=0
        l=len(nums)
        lowerNum = 1000000001
        while i <l :
            if lowerNum > nums[i]:
                lowerNum = nums[i]
            else:
                print(nums[i] , lowerNum, maxD)
                if nums[i]-lowerNum > maxD and nums[i] > lowerNum:
                    maxD = nums[i]-lowerNum
            i+=1
        return maxD
