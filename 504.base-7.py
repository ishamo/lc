class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        positive = True
        if num < 0:
            positive = False
            num = -1 * num

        if num == 0: return '0'

        result = ''
        while num >= 7:
            a, b = num / 7, num % 7
            result += str(b)
            num = a

        if num: result += str(num)

        if not positive:
            return '-' + result[::-1]
        return result[::-1]
#
#
# s = Solution()
# print s.convertToBase7(100)
#





