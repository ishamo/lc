class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = [0 for i in range(len(T))]
        stack = []
        for idx, item in enumerate(T):
            if not stack or stack[-1][1] >= item:
                stack.append((idx, item))
            else:
                while stack and stack[-1][1] < item:
                    index, val = stack.pop(-1)
                    result[index] = idx - index

                stack.append((idx, item))

        return result
#
#
# T = [73, 73, 75, 71, 69, 72, 76, 73]
# s = Solution()
# print s.dailyTemperatures(T)
