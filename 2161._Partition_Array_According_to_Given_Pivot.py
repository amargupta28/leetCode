class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low=[]
        med=[]
        high=[]

        for n in nums:
            if n< pivot:
                low.append(n)
            elif n == pivot:
                med.append(n)
            else:
                high.append(n)
        
        return low+med+high
