class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a={}
        b=0
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=[]
            a[nums[i]].append(i)
        for i in a.keys():
            b += (((len(a[i]))-1)*(len(a[i])))/2
        return int(b)    




formula used --> ((n-1)*n)/2
time complexity : O(N)
