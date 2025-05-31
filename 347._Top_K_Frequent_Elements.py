class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[[] for i in range(len(nums)+1)]
        count={}
        output=[]
        for i in nums:
            count[i] = 1+count.get(i,0)
         
        for key,v in count.items():
            res[v].append(key)
        print(res)
        
        for m in range(len(res)-1,0,-1):
            for j in res[m]:
                output.append(j)
                print(output , len(output),k,len(output) == k)
                if len(output) == k:
                    return output
       
