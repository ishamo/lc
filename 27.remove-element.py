class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0

        while True:
            before = len(nums)
            try:
                nums.remove(val)
            except:
                pass
            after = len(nums)
            if after == before: break

        return len(nums)
#
#
# s = Solution()
# alist = [3,2,2,3]
# s.removeElement(alist, 3)
# print(alist)
