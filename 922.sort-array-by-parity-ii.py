class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even, odd = [], []
        for item in A:
            if item % 2 == 0: even.append(item)
            else: odd.append(item)

        result = []
        for i in range(len(even)):
            result.append(even[i])
            result.append(odd[i])

        return result

