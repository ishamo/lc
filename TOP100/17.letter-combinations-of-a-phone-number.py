class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        mp = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = []
        if not digits: return result

        self.calculate_result(digits, 0, '', result, mp)
        return result

    def calculate_result(self, digits, pos, current, result, mp):
        if pos == len(digits):
            result.append(current)
            return
        else:
            for v in mp[digits[pos]]:
                self.calculate_result(digits, pos+1, current+v, result, mp)
