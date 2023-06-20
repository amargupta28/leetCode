class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        count=[0 for i in range(26)]
        
        for i in range(len(s)):
            count[ord(s[i])-97]+=1
            count[ord(t[i])-97]-=1
        for i in count:
            if i !=0:
                return False
        return True
