class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        counter= collections.Counter(s)
        
        if counter['A'] >= 2:
            return False
        
        for i in range(1,len(s)-1):
            if s[i] == "L":
                if s[i-1] == 'L' and s[i+1] == "L":
                    return False
        return True
            
