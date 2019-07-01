class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        DP = nums[:]
        for idx, i in enumerate(nums[1:], 1):
            if DP[idx-1] > 0:
                DP[idx] = DP[idx-1] + i
            else:
                DP[idx] = i

        return max(DP)
