class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        output=[]
        while i <len(nums1) and j <len(nums2):
            if nums1[i] < nums2[j]:
                output.append(nums1[i])
                i+=1
            else:
                output.append(nums2[j])
                j+=1
        
        while i <len(nums1):
            output.append(nums1[i])
            i+=1
        
        while j <len(nums2):
            output.append(nums2[j])
            j+=1
        if len(output) % 2 == 0:
            midpt=len(output)/2
            return (output[midpt]+output[midpt-1])/2.0
        else:
            midpt=int(len(output))/2
            return (output[midpt])/1.0
