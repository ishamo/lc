class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = set(nums)
        return (sum(nums)-sum(ns))/(len(nums)-len(ns))

