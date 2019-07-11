class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        arr = [0] * 256
        lens = len(s)
        mx = 0
        i, j = 0, 0
        while i < lens and j < lens:
            if arr[ord(s[j])] == 0:
                arr[ord(s[j])] = 1
                j += 1
                if j-i > mx:
                    mx = j-i

            else:
                arr[ord(s[i])] = 0
                i += 1

        return mx
#
# s = Solution()
# print s.lengthOfLongestSubstring('pwwkew')
# print s.lengthOfLongestSubstring('p')
