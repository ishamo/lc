class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if not s: return result
        lens = len(s)

        self.helper(s, 0, 1, lens-1, [], result)
        return result

    def helper(self, s, i, j, cut, current, result):
        if not self.isvalid(s[i:j+1]): return
        else:
            current = current[:] + [s[i:j+1]]
            if j == cut:
                result.append(current)
                return
            else:
                for k in range(2, len(s)-1-j):
                    self.helper(s, j+1, j+k, len(s)-1, current, result)

    def isvalid(self, s, i, j):
        while s[i] == s[j] and i < j:
            i += 1
            j -= 1

        return True if i >= j else False

