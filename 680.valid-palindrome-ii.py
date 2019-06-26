class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True

        lens = len(s)

        l, r = 0, lens-1
        while l <= r:
            if not s[l] == s[r]: break
            else:
                l += 1
                r -= 1

        # check l and r

