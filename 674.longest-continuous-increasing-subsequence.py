class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        lenn = len(nums)
        DP = [1] * lenn

        for i in range(1, lenn):
            if nums[i] > nums[i-1]:
                DP[i] = DP[i-1] + 1

        return max(DP)
