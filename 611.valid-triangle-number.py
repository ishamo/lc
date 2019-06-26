class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn = len(nums)
        if lenn < 3: return 0

        nums.sort()
        count = 0
        for third in range(2, lenn)[::-1]:
            l, r = 0, third-1
            while l < r:
                if nums[l] + nums[r] <= nums[third]:
                    l += 1
                else:
                    count += r - l
                    r -= 1

        return count

#
# nums = [2,2,3,4]
# s = Solution()
# print s.triangleNumber(nums)
