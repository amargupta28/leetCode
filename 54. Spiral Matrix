class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output=[]
        top=0
        bot =len(matrix)-1
        left=0
        right=len(matrix[0])-1
        
        while top <= bot and left <= right:
            for i in range(left,right+1):
                output.append(matrix[top][i])
            top+=1
            #print(output,1)
            
            for i in range(top,bot+1):
                output.append(matrix[i][right])
            right-=1
            #print(output,2,right,left,top,bot)
            
            if (top <= bot):
                for i in range(right,left-1,-1):
                    output.append(matrix[bot][i])
                bot-=1
                #print(output,3)
            if left <= right:
                for i in range(bot,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
                #print(output,4)
                    
                
        return (output)
                
        
        
