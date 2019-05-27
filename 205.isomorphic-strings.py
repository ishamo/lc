class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) == len(t): return False
        table = {}
        for idx, c in enumerate(s):
            if c not in table:
                table[c] = t[idx]
            else:
                if not table[c] == t[idx]: return False

        values = table.values()
        return True if len(set(values)) == len(values) else False
