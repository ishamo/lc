class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        nums.sort()
        lenn = len(nums)
        return sum([min(nums[i], nums[i+1]) for i in range(0, lenn, 2)])
