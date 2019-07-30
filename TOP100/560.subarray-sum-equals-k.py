# import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = sums = 0
        cnt = collections.Counter()
        for n in nums:
            cnt[sums] += 1
            sums += n
            ans += cnt[sums-k]
        return ans
#
#
# print Solution().subarraySum([1,1,1],2)
#
