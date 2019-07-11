# coding: utf-8
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        if not coins: return -1
        coins.sort()

        DP = [1000] * (amount+1)
        DP[0] = 0
        for i in range(amount+1):
            for c in coins:
                if not 0 <= i+c <= amount: break
                DP[i+c] = min(DP[i]+1, DP[i+c])

        return DP[amount] if DP[amount]<1000 else -1
