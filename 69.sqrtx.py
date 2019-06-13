class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        l, r = 1, x
        while l <= r:
            mid = (l+r)/2
            multify = mid * mid
            if multify == x: return mid
            elif multify < x:
                if (mid+1)*(mid+1)>x:
                    return mid
                l = mid
            else:
                r = mid

        return 1
#
#
# s = Solution()
# print s.mySqrt(4)
# print s.mySqrt(10)
# print s.mySqrt(9)
