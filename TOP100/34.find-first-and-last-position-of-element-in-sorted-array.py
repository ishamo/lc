class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)/2
            if nums[mid] == target:
                left, right = mid, mid
                while left-1>=0 and nums[left] == nums[left-1]:
                    left -= 1
                while right+1<len(nums) and nums[right] == nums[right+1]:
                    right += 1
                return [left, right]
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return [-1, -1]
                

# print Solution().searchRange([2,2], 3)
        
