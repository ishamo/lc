class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table = {}
        for n in nums:
            if not n in table:
                table[n] = 0
            table[n] += 1

        result = [[key, v] for key, v in table.items()]
        result = sorted(result, key=lambda item: item[1], reverse=True)
        return [item[0] for item in result[:k]]

# 
# nums = [1,1,1,2,2,3]
# k = 2
# print Solution().topKFrequent(nums, k)
# nums, k = [1], 1 
# print Solution().topKFrequent(nums, k)
#         
# 
# nums, k = [4,1,-1,2,-1,2,3], 2
# print Solution().topKFrequent(nums, k)

