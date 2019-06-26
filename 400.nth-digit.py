class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        interval = 9
        sm = 0
        while interval < n:
            sm += interval
            interval *= 10

        # 第n - sm个数字




#
s = Solution()
print s.findNthDigit(100000000)
# print s.findNthDigit(11)
#
