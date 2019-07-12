class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        lenn = len(nums)
        DP = [[nums[i] for i in range(lenn)] for j in range(2)]

        DP[0][0], DP[1][0] = nums[0], nums[0]

        for i in range(1, lenn):
            DP[0][i] = max(DP[0][i-1]*nums[i], DP[1][i-1]*nums[i], DP[0][i])
            DP[1][i] = min(DP[0][i-1]*nums[i], DP[1][i-1]*nums[i], DP[1][i])

        return max(item for ROW in DP for item in ROW)
#
#
# nums = [2,3,-2,4]
# nums = [-2,0,-1]
# nums = [2,-5,-2,-4,3]
# s = Solution()
# print s.maxProduct(nums)
