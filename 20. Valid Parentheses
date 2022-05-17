class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        
        for i in s:
            if len(stack)==0:
                stack.append(i)
            elif stack[-1] == '(' and i == ')':
                stack.pop()
            elif stack[-1] == '[' and i == "]":
                stack.pop()
            elif stack[-1] == "{" and i == "}":
                stack.pop()
            else:
                stack.append(i)
        return True if len(stack) == 0 else False
