class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[[] for i in range(len(s)+1)]
        temp = ""
        
        count={}
        for i in s:
            count[i] = 1+count.get(i,0)
        for key,val in count.items():
            res[val].append(key)
        # print(res)
        for m in range(len(res)-1,0,-1):
            for j in res[m]:
                 for l in range(m):
                        # print(j)
                        temp+=j
        return (temp)
     
