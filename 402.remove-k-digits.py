# coding: utf-8
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        lenc = len(num)
        if not num or lenc <= k: return '0'

        stack = []
        for i in range(lenc):
            if not stack:
                stack.append(num[i])
            else:
                # print('stack, len, need, last, current', stack, len(stack)+lenc-(i+1), lenc-k, stack[-1], num[i])
                while stack and len(stack) + lenc - (i+1) >= lenc - k and int(stack[-1]) > int(num[i]):
                    stack.pop(-1)
                stack.append(num[i])
        return ''.join(stack[0:lenc-k]).lstrip('0') or '0'


# s = Solution()
# print s.removeKdigits('1432219', 3)
# print s.removeKdigits('112', 1)
