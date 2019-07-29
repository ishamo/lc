# coding: utf-8
# 这段代码我之前一下就写出来了，现在竟然怎么想都想不出来，脑力退化了吗？
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 4,5,6,7,0,1,2,3
        if not nums: return -1

        lenn = len(nums)

        l, r = 0, lenn-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target: return mid
            elif nums[mid] > nums[l]:
                if nums[mid] > target > nums[l]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[mid] < target < nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1


nums = [4,5,6,7,0,1,2,3]
print Solution().search(nums, 6)
