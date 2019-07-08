class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums: return result
        self.helper(nums, result, [], 0)
        return result

    def helper(self, nums, result, path, idx):
        if idx == len(nums):
            result.append(path[:])
            return
        else:
            self.helper(nums, result, path[:], idx+1)
            self.helper(nums, result, path[:] + [nums[idx]], idx+1)
