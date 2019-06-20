class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if not S: return []

        index = []
        for idx, item in enumerate(S):
            if item == C: index.append(idx)

        result = []

        for idx, item in enumerate(S):
            result.append(self.find_closest(idx, index))

        return result

    def find_closest(self, target, nums):
        return min(map(lambda x: abs(x - target), nums))
