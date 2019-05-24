class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr = str(num)
        while len(numstr) > 1:
            nums = [int(item) for item in list(numstr)]
            numstr = str(sum(nums))

        return int(numstr)

