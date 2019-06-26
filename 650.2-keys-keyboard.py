# coding: utf-8
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        DP = [0xfffff] * (n+1)
        DP[1] = 0
        DP[2] = 2
        LAST = [0] * (n+1)  # 记录最后一次copy了几个A
        LAST[2] = 1
        # DP[i]: 有n个A需要执行的最少操作次数
        # if last + k == n: DP[i] = DP[k] + 1
        # if k * 2 == n: DP[i] = DP[k] + 2

        for i in range(1, n+1):
            for j in range(1, i):
                if LAST[j] + j == i:
                    DP[i] = min(DP[j] + 1, DP[i])
                if j * 2 == i and DP[i] > DP[j] + 2:
                    DP[i] = DP[j] + 2
                    LAST[i] = j

        return DP[n]
