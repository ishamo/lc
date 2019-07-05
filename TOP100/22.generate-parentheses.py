class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        if n == 0: return result

        self.helper(n, n, '', result)

        return result

    def helper(self, lc, rc, path, result):
        if lc > rc: return
        elif lc < 0 or rc < 0: return
        elif lc == 0 and rc == 0:
            result.append(path)
            return
        else:
            self.helper(lc-1, rc, path+'(', result)
            self.helper(lc, rc-1, path+')', result)
# 
# 
#         
# s = Solution()
# print s.generateParenthesis(3)
