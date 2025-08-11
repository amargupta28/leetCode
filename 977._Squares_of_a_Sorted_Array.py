class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp=[-1]*len(nums)
        l=0
        r=len(nums)-1
        pos=len(nums)-1

        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                temp[pos] = nums[l]**2
                l+=1
            
            else:
                temp[pos]= nums[r]**2
                r-=1
            
            pos-=1
        return temp

#o(n) ....it is sorted array so two pointers
