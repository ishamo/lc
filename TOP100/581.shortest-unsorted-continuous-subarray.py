class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        cp = nums[:]
        cp.sort()
        lens = len(cp)
        i, j = 0, lens-1

        while i <= j and cp[i] == nums[i]:
            i += 1
        while i <= j and cp[j] == nums[j]:
            j -= 1

        return j-i+1
