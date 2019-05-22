class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        table = {}
        for x in J: table[x] = 1
        count = 0
        for s in S:
            if s in table:
                count += 1

        return count

