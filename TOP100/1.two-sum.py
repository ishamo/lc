class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return []
        table = {}
        for idx, i in enumerate(nums):
            if i not in table:
                table[i] = []
            table[i].append(idx)

        for idx, n in enumerate(nums):
            if target-n in table:
                other = set(table[target-n]) - set([idx])
                if other:
                    return [idx, list(other)[0]]

        return []




