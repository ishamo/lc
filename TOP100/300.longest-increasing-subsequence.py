class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        DP = [1] * len(nums)

        for idx, item in enumerate(nums):
            for j in range(idx):
                if nums[idx] > nums[j]:
                    DP[idx] = max(DP[idx], DP[j] + 1)

        return max(DP)
#
#
# nums = [10,9,2,5,3,7,101,18]
# s = Solution()
# print s.lengthOfLIS(nums)
#
