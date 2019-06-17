class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in list(str(int(''.join([str(item) for item in digits])) + 1))]
