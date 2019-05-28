class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        if  len(nums) == 1: return True
        lenn = len(nums)
        DP = [0] * len(nums)
        DP[0] = nums[0]
        for i in range(1, lenn):
            if DP[i-1] < 1: DP[i] = 0
            else:
                DP[i] = max(DP[i-1]-1, nums[i])

        # print 'DP', DP
        return DP[-2] >= 1
