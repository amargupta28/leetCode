class SparseVector:
    def __init__(self, nums: List[int]):
        self.t=nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        s=0
        for i in range(len(self.t)):
            s+=self.t[i] * vec.t[i]
        
        return s

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
