class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        lenn = len(nums)

        cnt = lenn
        start = 1
        while start < cnt:
            # print('start, nums', start, nums)
            if nums[start] == nums[start-1]:
                if start+1 < lenn:
                    nums[start:cnt] = nums[start+1:cnt+1]

                cnt -= 1
            else:
                start += 1


        return cnt
#
# nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [0,0,1,1,1,2,2,3,3,4]
# s = Solution()
# ret = s.removeDuplicates(nums)
# print nums, ret
