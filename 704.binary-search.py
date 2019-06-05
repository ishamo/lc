class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        lenn = len(nums)
        l, r = 0, lenn - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target: return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

