class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        self.helper(nums, [], result)
        return result

    def helper(self, nums, path, result):
        if len(path) == len(nums):
            result.append(path[:])
            return result
        else:
            release = [i for i in nums if i not in path]
            for r in release:
                path.append(r)
                self.helper(nums, path, result)
                path.pop(-1)
