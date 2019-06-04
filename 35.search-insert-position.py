class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, e in enumerate(nums):
            if target <= e: return idx

        return len(nums)
