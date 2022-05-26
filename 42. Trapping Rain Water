class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        lmax=[-1]*len(height)
        rmax=[-1]*len(height)
        lmax[0] =height[0]
        rmax[-1]=height[-1]
        for i in range(1,len(height)):
            lmax[i] = max(lmax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rmax[i]=max(rmax[i+1],height[i])
        print(rmax)
        print(lmax)
        for i in range(0,len(height)):
            res+= min(lmax[i],rmax[i]) -height[i]
        return (res)
