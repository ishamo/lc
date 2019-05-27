class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for idx, n in enumerate(nums):
            table[n] = idx

        for idx, n in enumerate(nums):
            other = target - n
            if other in table and not table[other] == idx:
                return [idx, table[other]]

        return [0, 1]

