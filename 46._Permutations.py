class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        if len(nums) <1:
            return [nums[:]]
        for i in range(len(nums)):
            temp=nums.pop(0)
            res=self.permute(nums)
            for item in res:
                item.append(temp)
            result.extend(res)
            nums.append(temp)
        return result
            
