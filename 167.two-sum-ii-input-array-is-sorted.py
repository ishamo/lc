class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenn = len(numbers)

        i, j = 0, lenn-1
        while i < j:
            sm = numbers[i] + numbers[j]
            if sm == target:
                return [i+1, j+1]
            elif sm > target:
                j -= 1
            else:
                i += 1

        return [-1, -1]


