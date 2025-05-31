class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <2:
            return intervals
        intervals.sort()
        arr=[]
        for i in intervals:
            if arr == [] or arr[-1][1] < i[0]:
                arr.append(i)
            else:
                arr[-1][1] = max(arr[-1][1],i[1])
        return arr
