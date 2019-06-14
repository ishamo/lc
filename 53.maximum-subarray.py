class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        lenn = len(nums)
        DP = [i for i in nums]

        for i in range(1, lenn):
            if DP[i-1] > 0:
                DP[i] = DP[i-1] + nums[i]

        return max(DP)
