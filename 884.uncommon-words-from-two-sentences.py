class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        ret = []
        tableA, tableB = {}, {}
        for k in A:
            if k not in tableA:
                tableA[k] = 1
            else:
                tableA[k] += 1

        for k in B:
            if k not in tableB:
                tableB[k] = 1
            else:
                tableB[k] += 1

        # print(tableA, tableB, ret)
        for k in tableA:
            if k not in tableB and tableA[k] == 1:
                ret.append(k)

        for k in tableB:
            if k not in tableA and tableB[k] == 1:
                ret.append(k)

        return ret
#
#
# a, b = "apple apple", "banana"
# a, b = "s z z z s", "s z ejt"
#
# s = Solution()
# print s.uncommonFromSentences(a,b)
