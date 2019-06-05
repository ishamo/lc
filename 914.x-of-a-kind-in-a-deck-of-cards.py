class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        table = {}
        for d in deck:
            if d not in table:
                table[d] = 0
            table[d] += 1

        g = reduce(self.gcd, table.values())
        if g < 2: return False

        return True

    def gcd(self, a, b):
        if b != 0:
            return self.gcd(b, a %  b)
        return a
