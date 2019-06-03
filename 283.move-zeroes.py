class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        count0 = 0
        idx = 0
        while idx < lenn:
            if nums[idx] == 0:
                count0 += 1
            else:
                if count0 > 0:
                    nums[idx], nums[idx-count0] = nums[idx-count0], nums[idx]

            idx += 1
