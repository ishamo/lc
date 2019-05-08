class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        DP = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and DP[i] < DP[j] + 1:
                    DP[i] = DP[j] + 1
        return max(DP)


# [-2, -1]
