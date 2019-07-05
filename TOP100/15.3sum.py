class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lenn = len(nums)
        result = []
        if lenn < 3: return result

        for i in range(0, lenn-2):
            j, k = i+1, lenn-1
            if i > 0 and nums[i] == nums[i-1]: continue
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif sum3 > 0:
                    k -= 1
                else:
                    j += 1

        return result
# 
#         
# nums = [-1, 0, 1, 2, -1, -4]
# s = Solution()
# print s.threeSum(nums)
