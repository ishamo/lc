class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]

        sm = ''
        for idx, c in enumerate(num1):
            result =  self.multiply_by_char(num2, c)
            result = '0' * idx + result
            sm = self.add(sm, result)

        return sm[::-1]

    def multiply_by_char(self, num, char):
        result = ''
        c = 0
        for n in num:
            m = int(n) * int(char) + c
            p = m % 10
            result += '%s' % p
            c = m / 10
        if c:
            result += '%s' % c
        return result

    def add(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        if len1 > len2:
            str1, str2 = str2, str1
            len1, len2 = len2, len1

        result = ''
        c = 0
        for idx, char in enumerate(str1):
            sm = int(char) + int(str2[idx]) + c
            result += '%s' % (sm % 10)
            c = sm / 10
        for char in str2[len1:len2]:
            sm = int(char) + c
            result += '%s' % (sm % 10)
            c = sm / 10
        if c:
            result += '%s' % c
        return result
