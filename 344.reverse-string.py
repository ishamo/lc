class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s: return

        lens = len(s)
        i, j = 0, lens-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return
