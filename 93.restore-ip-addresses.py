class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        lens = len(s)
        if lens < 4: return result

        self.helper(s, result, 0, [])
        return list(set(result))

    def helper(self, release, result, k, current):
        if k == 4:
            if not release and self.isvalid(current):
                result.append('.'.join(current))
                return
        else:
            for i in range(1, 4):
                self.helper(release[i:], result, k+1, current[:] + [release[0:i]])

    def isvalid(self, current):
        if not len(current) == 4: return False
        if any(map(lambda x: len(x) >= 2 and x.startswith('0'), current)): return False
        if all(map(lambda x: x and 0 <= int(x) <= 255, current)): return True
        return False
#
#
# s = Solution()
# print s.restoreIpAddresses("0000")
