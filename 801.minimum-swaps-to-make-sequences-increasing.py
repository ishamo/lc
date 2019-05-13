class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A: return 0
        results = []
        self.doswap(A, B, 0, 0, results)
        return min(results)

    def doswap(self, A, B, cnt, i, results):
        _A, _B = A[:], B[:]
        if i == len(A) - 1:
            if self.isValid(_A) and self.isValid(_B): results.append(cnt)
            else:
                _A[i], _B[i] = _B[i], _A[i]
                if self.isValid(_A) and self.isValid(_B): results.append(cnt+1)
        else:
            self.doswap(_A, _B, cnt, i+1, results)
            _A[i], _B[i] = _B[i], _A[i]
            self.doswap(_A, _B, cnt+1, i+1, results)

    def isValid(self, array):
        if not array: return True
        for i in range(1, len(array)):
            if not array[i] > array[i-1]: return False
        return True
A, B = [1,2,4,8,10,12,14,15,16,18,20,24,26,27,32,33,35,36,39,40], [0,5,6,8,10,13,14,15,17,21,23,25,26,27,30,32,34,37,38,39]
#
#
s = Solution()
print s.minSwap(A, B)
