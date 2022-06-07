    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        for index,ch in enumerate(s):
            if counter[ch] == 1:
                return index
        return -1
