class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <2:
            return False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False
