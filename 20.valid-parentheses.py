class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        table = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        if not s: return True
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack or not stack[-1] == table[c]: return False
                stack.pop(-1)

        if stack: return False
        return True

