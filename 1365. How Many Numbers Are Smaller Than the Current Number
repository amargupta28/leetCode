class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        brr= sorted(nums)
        dit={}
        temp=[]
        for i,v in enumerate(brr):
            if v not in dit:
                dit[v] = i
        
        for i in nums:
            temp.append(dit[i])
        return temp
                
