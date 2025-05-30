class Solution:
    def secondHighest(self, s: str) -> int:
        n=[]
        for i in s:
            if i.isnumeric():
                n.append(int(i))
        first=-1
        second = -1

        for i in n:
            if i > first:
                second=first
                first = i
            elif i> second and i!= first:
                second = i
        
        return second
