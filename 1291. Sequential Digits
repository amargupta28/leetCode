class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        lowlength= len(str(low))
        highLength = len(str(high))
        arr=[]
        num="123456789"
        for i in range(lowlength,highLength+1):
            for j in range(len(num)-i+1):
                temp=int(num[j:j+i])
                #print(int(temp),i)
                if high >= temp and temp >= low:
                    arr.append(temp)
        return arr
