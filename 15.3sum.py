class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        lenn = len(nums)
        if lenn < 3: return result

        nums.sort()
        # print('nums', nums)
        for i in range(0, lenn-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i+1, lenn-1
            while i < j < k:
                sm = nums[i] + nums[j] + nums[k]
                if sm == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    k -= 1
                    j += 1
                    while k > j and nums[k+1] == nums[k]:
                        k -= 1
                    while j < k and nums[j-1] == nums[j]:
                        j += 1

                elif sm > 0:
                    k -= 1
                else:
                    j += 1

        return result
#
#
# arr = [-1,0,1,2,-1,-4]
#
# s = Solution()
# print s.threeSum(arr)
