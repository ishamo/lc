class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        negtive = True if x[0] == '-' else False

        if negtive:
            x = -1 * int(x[1:][::-1])
        else: x = int(x[::-1])

        # print('x', x)
        if x < -pow(2,31) or x > pow(2,31)-1: return 0
        return x


# x = -123
# s = Solution()
# print s.reverse(x)
