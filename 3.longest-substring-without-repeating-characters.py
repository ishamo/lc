class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        i, j = 0, 0
        arr = [0] * 256
        mx = 0
        while i < length and j < length:
            # print('i, j', i, j, s, s[i], s[j])
            if arr[ord(s[j])] == 0:
                arr[ord(s[j])] = 1
                j += 1
                mx = j - i if j - i > mx else mx
            else:
                arr[ord(s[i])] = 0
                i += 1
        return mx


# if __name__ == '__main__':
#     s = Solution()
#     print s.lengthOfLongestSubstring('pwwkew')
