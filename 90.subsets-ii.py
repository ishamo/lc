class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = set()
        if not nums: return list(result)

        self.helper(nums, 0, [], result)
        return [list(item) for item in result]

    def helper(self, nums, i, current, result):
        if i == len(nums):
            result.add(tuple(current))
            return
        else:
            self.helper(nums, i+1, current, result)
            current.append(nums[i])
            self.helper(nums, i+1, current, result)
            current.pop(-1)
#
#
# s = Solution()
# print s.subsetsWithDup([1, 2, 2])
#
