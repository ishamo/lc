class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []
        if not S: return result
        lens = len(S)

        i = 0

        self.enum_every_char(S, i, lens, result, '')

        return result

    def enum_every_char(self, S, i, lens, result, current):
        if i == lens:
            result.append(current)
            return
        else:
            if 'A' <= S[i].upper() <= 'Z':
                self.enum_every_char(S, i+1, lens, result, current+S[i].lower())
                self.enum_every_char(S, i+1, lens, result, current+S[i].upper())
            else:
                self.enum_every_char(S, i+1, lens, result, current+S[i])
