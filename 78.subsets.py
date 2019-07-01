class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        if not nums: return result

        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, i, current, result):
        if i == len(nums):
            result.append(current[:])
            return
        else:
            self.helper(nums, i+1, current, result)
            current.append(nums[i])
            self.helper(nums, i+1, current, result)
            current.pop(-1)
#
#
# s = Solution()
# print s.subsets([1, 2, 3])
