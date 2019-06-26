class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        new_str = ''
        for c in s:
            if 'A' <= c.upper() <= 'Z':
                new_str += c.upper()

        lens = len(new_str)
        l, r = 0, lens
        while l <= r:
            if not new_str[l] == new_str[r]: return False
            l += 1
            r -= 1

        return True
