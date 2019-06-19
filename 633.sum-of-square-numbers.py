class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0: return False

        end = int(pow(c, 1.0/2))
        left, right = 0, end

        while left <= right:
            t = left * left + right * right
            if t == c: return True
            elif t > c: right -= 1
            else:
                left += 1

        return False


# s = Solution()
# s.judgeSquareSum(5)
#
