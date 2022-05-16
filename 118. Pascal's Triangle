class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        print([0]+res[-1]+[0])
        
        for i in range(numRows-1):
            temp = [0]+res[-1]+[0]
            tempArr=[]
            for i in range(len(temp)-1):
                tempArr.append(temp[i]+temp[i+1])
            res.append(tempArr)
                
        return res
                
