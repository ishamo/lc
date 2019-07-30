class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums: return 0
        sm = ans = 0
        table = {}
        table[0] = 1
        for n in nums:
            sm += n
            if sm not in table:
                table[sm] = 0
            table[sm] += 1

            if sm-k in table:
                ans += table[sm-k]

        return ans
#
#
# print Solution().subarraySum([1,1,1],2)
#
