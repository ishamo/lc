class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        if num & num - 1: return False
        while num > 1:
            num = num >> 2
        if not num == 1: return False
        return True
#
#
# s = Solution()
# print s.isPowerOfFour(3)
# print s.isPowerOfFour(8)
