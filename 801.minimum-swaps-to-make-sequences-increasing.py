# coding: utf-8
class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        swap, keep = [99999999] * len(A), [99999999] * len(A)
        swap[0], keep[0] = 1, 0
        for i in range(1, len(A)):

            if A[i]>A[i-1] and B[i]>B[i-1]:
                swap[i] = swap[i-1] + 1
                keep[i] = keep[i-1]

            if A[i]>B[i-1] and B[i]>A[i-1]:
                swap[i] = min(swap[i], keep[i-1]+1)
                keep[i] = min(keep[i], swap[i-1])

        return min(swap[-1], keep[-1])


# A, B = [1,2,4,8,10,12,14,15,16,18,20,24,26,27,32,33,35,36,39,40], [0,5,6,8,10,13,14,15,17,21,23,25,26,27,30,32,34,37,38,39]
# A, B = [1, 3, 5, 4], [1, 2, 3, 7]
# A, B = [1, 4, 3, 4, 7], [1, 2, 5, 6, 5]
#
#
# A, B = [0,3,5,8,9], [2,1,4,6,9]
# s = Solution()
# print s.minSwap(A, B)
