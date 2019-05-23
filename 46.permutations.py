class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return []
        result = []
        lenn = len(nums)
        pool = list(range(lenn))

        def enum_value(current, pool):
            if len(pool) == 1:
                current.append(nums[pool[0]])
                result.append(current)
                return
            else:
                for p in pool:
                    tmp = pool[:]
                    tmp.remove(p)
                    enum_value(current + [nums[p]], tmp)

        enum_value([], pool)
        return result
