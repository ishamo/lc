# coding: utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lena = len(a)
        lenb = len(b)
        if not lena: return b
        if not lenb: return a
        if lena > lenb: a, b = b, a
        a = a[::-1]
        b = b[::-1]

        c = '0'
        result = ''
        for idx, char in enumerate(a):
            out, c = self.add_bit(char, b[idx], c)
            result += out

        for char in b[len(a):]:
            out, c = self.add_bit('0', char, c)
            result += out

        if c == '1':
            result += c
        return result[::-1]

    def add_bit(self, a, b, c):
        """ result, c """
        if c == '0':
            if a == '0' and b == '0': return '0', '0'
            elif a != b: return '1', '0'
            else: return '0', '1'
        else:
            if a == '0' and b == '0': return '1', '0'
            elif a != b: return '0', '1'
            else: return '1', '1'

#
# s = Solution()
# print s.addBinary('1010', '1011')


#   ✘ Wrong Answer
#   ✘ 76/294 cases passed (N/A)
#   ✘ testcase: '"1010"\n"1011"'
#   ✘ answer: "11001"
#   ✘ expected_answer: "10101"

