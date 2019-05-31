class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lens = len(s)
        result = ''
        for i in range(0, lens+1, 2*k):
            result += s[i:i+k][::-1]
            result += s[i+k:i+2*k]

        return result
#
#
# s = Solution()
# astr = 'abcdefg'
# print s.reverseStr(astr, 2)
#
#
