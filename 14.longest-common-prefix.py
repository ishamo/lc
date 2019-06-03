class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        return reduce(self.commonOfTwo, strs)

    def commonOfTwo(self, s1, s2):
        if not s1 or not s2: return ''

        len1, len2 = len(s1), len(s2)
        ret = ''
        for i in range(min(len1, len2)):
            if s1[i] == s2[i]:
                ret += s1[i]
            else:
                break

        return ret
#
#
# s = Solution()
# print s.longestCommonPrefix([])
