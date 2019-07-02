class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        lenn = len(nums)

        MP = [[0 for i in range(2)] for j in range(lenn)]

        MP[0][0] = 0
        MP[0][1] = nums[0]

        for i in range(1, lenn):
            MP[i][0] = max(MP[i-1][0], MP[i-1][1], 0)
            MP[i][1] = max(MP[i-1][0], 0) + nums[i]

        return max(0, MP[lenn-1][0], MP[lenn-1][1])
# 
# 
# nums = [1,2,3,1]
# s = Solution()
# print s.rob(nums)
# nums = [2,7,9,3,1]
# print s.rob(nums)
# 
