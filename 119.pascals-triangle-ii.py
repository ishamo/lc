class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #      1
        #      1   1
        #      1   2   1
        #      1   3   3   1
        table = [[ 0 for i in range(rowIndex+1)] for j in range(rowIndex+1)]
        table[0][0] = 1
        for i in range(1, rowIndex+1):
            for j in range(rowIndex+1):
                if j == 0 or j == rowIndex: table[i][j] = 1
                else:
                    table[i][j] = table[i-1][j-1] + table[i-1][j]

        return table[rowIndex]
#
#
# s = Solution()
# print s.getRow(0)
# print s.getRow(1)
# print s.getRow(2)
# print s.getRow(3)
# print s.getRow(4)
