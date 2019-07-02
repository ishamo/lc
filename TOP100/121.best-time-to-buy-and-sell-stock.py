class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0

        mx = 0
        small = prices[0]

        for i in prices[1:]:
            if i < small: small = i
            if i - small > mx: mx = i-small

        return mx
# 
# 
# s = Solution()
# nums = [7,1,5,3,6,4]
# print s.maxProfit(nums)
# nums = [7,6,4,3,2,1]
# print s.maxProfit(nums)
