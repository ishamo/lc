class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums or len(nums) == 1: return 0
        summerize0 = [0] * 100
        summerize1 = [0] * 100

        mask = 1

        for i in range(100):
            for n in nums:
                if n & mask:
                    summerize1[i] += 1
                else:
                    summerize0[i] += 1

            mask = mask << 1

        result = 0
        for i in range(100):
            result += summerize0[i] * summerize1[i]

        return result
#
#
# arr = [1337,7331]
# s = Solution()
# print s.totalHammingDistance(arr)
