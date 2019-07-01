class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        last = None
        for i in nums:
            if last is None:
                last = i
                count = 1
            elif i == last:
                count += 1
            else:
                count -= 1
                if count == 0:
                    last = None

        return last
