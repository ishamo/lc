class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        table = {}
        slist = str.split()
        if not len(slist) == len(pattern): return False
        for idx, p in enumerate(pattern):
            if p not in table:
                table[p] = slist[idx]
            else:
                if table[p] != slist[idx]: return False

        values = table.values()
        if len(set(values)) < len(values): return False

        return True
