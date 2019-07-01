class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if not s: return result
        lens = len(s)

        self.helper(s, 0, [], result)
        return result

    def helper(self, s, i, current, result):
        # print 'i, current, result', i, current, result
        if i == len(s):
            result.append(current[:])  # 这里必须是current的一个副本，不然回溯到最后, current肯定会被清掉！！！
        else:
            for j in range(i+1, len(s)+1):
                if self.isvalid(s[i:j]):
                    current.append(s[i:j])
                    self.helper(s, j, current, result)
                    current.pop(-1)

    def isvalid(self, s):
        if not s: return False
        lens = len(s)
        i, j = 0, lens-1
        while i < j and s[i] == s[j]:
            i += 1
            j -= 1
        return True if i >= j else False
#
#
# s = Solution()
# print s.partition('aab')
