class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums: return result

        lenn = len(nums)
        left, right = [], []
        left.append(1)
        right.append(1)
        for idx, item in enumerate(nums):
            left.append(left[-1] * nums[idx])
            right.append(right[-1] * nums[lenn-idx-1])

        right.reverse()

        for i in range(lenn):
            result.append(left[i] * right[i+1])

        return result
#
#
# print Solution().productExceptSelf([1,2,3,4])
#
