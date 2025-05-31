class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a=[0]*26
        for i in sentence:
            a[ord(i)-97]+=1
    
        for i in a:
            if i == 0:
                return False
        
        return True


Complexity: O(N)
