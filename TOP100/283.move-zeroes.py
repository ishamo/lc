class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        lenn = len(nums)
        tail = lenn
        check = 0
        while True:
            if check == tail: break
            else:
                if nums[check] == 0:
                    nums[check:tail-1] = nums[check+1:tail]
                    tail -= 1
                    nums[tail] = 0
                else:
                    check += 1

# 
# s = Solution()
# nums = [0,1,0,3,12]
# s.moveZeroes(nums)
# print nums

            
