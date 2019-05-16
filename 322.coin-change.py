class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount < 0: return -1
        DP = [1000] * (amount+1)
        DP[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if not 0 <= i-c <= amount: continue
                if DP[i - c] < 1000:
                    DP[i] = min(DP[i], DP[i-c]+1)

        return DP[amount] if DP[amount] < 1000 else -1
# s = Solution()
# print s.coinChange([2147483647], 2)
