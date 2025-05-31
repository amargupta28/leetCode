class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = sorted(nums1)
        n2= sorted(nums2)
        temp=[]
        i=0
        j=0 
        while i <len(n1) and j< len(n2):
            if n1[i] < n2[j]:
                i+=1
            elif n1[i] > n2[j]:
                j+=1
            else:
                temp.append(n1[i])
                i+=1
                j+=1
        return temp
