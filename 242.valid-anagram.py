class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s and not t: return True
        lens, lent = len(s), len(t)
        if not lens == lent: return False

        alist = [0] * 26
        blist = [0] * 26

        for i in s:
            alist[ord(i)-ord('a')] += 1

        for j in t:
            blist[ord(j)-ord('a')] += 1

        for k in range(len(alist)):
            if not alist[k] == blist[k]: return False

        return True
