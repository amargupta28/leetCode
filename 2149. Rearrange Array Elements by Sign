class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pnum=[]
        nnum=[]
        for i in nums:
            if i > 0 :
                pnum.append(i)
                continue
            nnum.append(i)

        j=0
        for i in pnum:
            if j > len(nums):
                break
            nums[j] = i
            j+=2
            
        
        j=1
        for i in nnum:
            if j> len(nums):
                break
            nums[j]=i
            j+=2
            
        return nums


Complexity: O(N)
