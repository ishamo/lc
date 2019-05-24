class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {}
        for n in nums:
            if n not in table: table[n] = 1
            else:
                return True

        return False
