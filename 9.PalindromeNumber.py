class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        reversed_digit=0
        y=x
        while x!=0:
            digit= x%10
            reversed_digit = reversed_digit*10+digit
            x//=10
        print(reversed_digit)
        
        return True if y == reversed_digit else False



# another solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
      s=str(x)
      i=0
      j=len(s)-1
      while i<=j:
          if s[i] != s[j]:
              return False
          i+=1
          j-=1
      return True
      
