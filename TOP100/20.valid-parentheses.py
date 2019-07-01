class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        old = s
        while True:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
            if s == old:
                break
            old = s

        return not s

