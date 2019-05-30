class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        lena = len(A)
        if lena <= 1: return True

        idm = 0  # 0: unknown, 1: increasing, 2: decreasing

        for i in range(1, lena):
            if A[i] > A[i-1]:
                if idm == 2:
                    return False
                idm = 1

            if A[i] < A[i-1]:
                if idm == 1:
                    return False
                idm = 2

        return True


