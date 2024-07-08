class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        i=0
        j=0

        while i <len(word1) and j<len(word2):
            result=result+word1[i]+word2[j]
            i+=1
            j+=1
        
        if i< len(word1):
            result=result+word1[i:]
        if j <len(word2):
            result=result+word2[j:]
        return result


Complexity: O(m+n)




---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        num=[0]*((len(word1))+len(word2))
        w1=[i for i in word1]
        w2=[i for i in word2]
        flag=1
        if len(word1) < len(word2):
            k=0
            flag=2
            for i in word1:
                if k>len(num):
                    break
                num[k]=i
                k+=2
        else:
            k=1
            flag=1
            for i in word2:
                if k>len(num):
                    break
                num[k]=i
                k+=2

        print(num)
        for i in range(len(num)-1,-1,-1):
            if num[i] != 0:
                continue
            print(i)
            num[i] = w1.pop() if flag == 1 else w2.pop()
            i-=1
        
        print(num)
        
        
        s=""
        for i in num:
            s+=i
        return s 



Complexity: O(N)
