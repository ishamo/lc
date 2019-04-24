class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0] * 26
        for i in s:
            arr[ord(i)-ord('a')] += 1
        for idx, i in enumerate(s):
            if arr[ord(i)-ord('a')] == 1:
                return idx
        return -1
