# coding: utf-8
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''

        lens = len(s)

        stack = []

        for c in s:
            if self.isdigit(c):
                if stack and self.isnumber(stack[-1]):
                    value = self.constract_number(stack[-1], c)
                    stack[-1] = value
                else:
                    stack.append(self.constract_number(0, c))

            elif c == ']':
                # 展开
                tmp = ''
                while stack and stack[-1] != '[':
                    tmp += stack[-1]
                    stack.pop(-1)

                stack.pop(-1)  # pop '['
                number = stack.pop(-1)
                tmp = tmp[::-1]
                stack.extend(list(number * tmp))

            else:
                stack.append(c)

        # print(stack)
        return ''.join(stack)

    def isdigit(self, c):
        return ord('0') <= ord(c) <= ord('9')

    def isnumber(self, n):
        return all(map(self.isdigit, list(str(n))))

    def constract_number(self, n, c):
        return n*10 + int(c)
# 
# s = "3[a]2[bc]"
# print s, Solution().decodeString(s)
# s = "3[a2[c]]"
# print s, Solution().decodeString(s)
# s = "2[abc]3[cd]ef"
# print s, Solution().decodeString(s)
