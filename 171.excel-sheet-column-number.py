class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        lens = len(s)
        result = 0

        for idx, char in enumerate(s):
            result += (ord(char)-ord('A')+1) * pow(26, lens-idx-1)

        return result
#
#
# s = Solution()
# print s.titleToNumber('A')
# print s.titleToNumber('B')
#

