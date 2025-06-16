class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for word in strs:
            count=[0]*26
            for i in word:
                count[ord(i) -97] +=1
            
            res[tuple(count)].append(word)
        
        return list(res.values())



#time complexity : o(m*n) m =length of array and n is average length of words
