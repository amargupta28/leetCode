class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        maxL=0
        maxR=0
        output=0
        while i <j:
            temp= min(height[i],height[j]) * (j-i)
            if output < temp:
                output=temp
                
            if height[i] > maxL:
                maxL=height[i]
            if height[j] > maxR:
                maxR=height[j]
            if height[i] >height[j]:
                j-=1
            else:
                i+=1
            
        print(output)
        return output
