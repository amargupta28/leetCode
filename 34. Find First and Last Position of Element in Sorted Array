class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lowerBound= self.check(nums,target,True)
        if lowerBound == -1:
            return [-1,-1]
        upperBound = self.check(nums,target,False)
        
        return [lowerBound,upperBound]
        
    def check(self,nums,target,bound):
        start=0
        end=len(nums)-1
        while start <= end:
            mid = (start+end)//2
            
            if nums[mid] == target:
                if bound:
                    if mid == start or nums[mid - 1] < target:
                        return mid
                    end = mid-1
                else:
                    if mid == end or nums[mid+1] > target:
                        return mid
                    start = mid+1
            elif nums[mid] > target:
                end =mid-1
            else:
                start = mid+1
        return -1
        
