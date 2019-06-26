class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        if k > n: return result

        pool = list(range(1, n+1))

        self.helper(pool, result, [], k)

        return result

    def helper(self, pool, result, current, k):
        if len(current) == k:
            result.append(current)
            return

        release = [i for i in pool if i not in current]
        for it in release:
            if not current or it > current[-1]:
                self.helper(pool, result, current[:] + [it], k)


s = Solution()
print s.combine(20, 16)
