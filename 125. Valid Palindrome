class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for i in s:
            if i.isalnum():
                temp+=i.lower()
        i=0
        j=len(temp)-1
        while i <j :
            print(i,j)
            if temp[i] != temp[j]:
                return False
            i+=1
            j-=1
        return True
