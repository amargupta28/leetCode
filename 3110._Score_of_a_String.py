class Solution:
    def scoreOfString(self, s: str) -> int:
        s1=0

        for i in range(len(s)-1):
            s1+=abs(ord(s[i]) - ord(s[i+1]))
        return s1


or

class Solution:
    def scoreOfString(self, s: str) -> int:
        a=[0]*len(s)
        for i in range(len(s)):
            a[i] =ord(s[i])
        
        s1=0
        print(a)
        for i in range(len(a)-1):
            t=a[i]-a[i+1]
            if t <0:
                t=t*-1
            s1=s1+t
            
        
        return s1
