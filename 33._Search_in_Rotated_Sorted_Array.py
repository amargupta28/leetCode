class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        
        while start <=end:
            midpt=(start+end)//2
            
            if target == nums[midpt]:
                return midpt
            elif nums[midpt] >= nums[start]:
                if target >= nums[start] and target < nums[midpt]:
                    end=midpt-1
                else:
                    start=midpt+1
            else:
                if target <= nums[end] and target > nums[midpt]:
                    start = midpt+1
                else:
                    end=midpt-1
        return -1
        
