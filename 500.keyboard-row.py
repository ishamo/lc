class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        if not words: return result

        for w in words:
            if self.isvalid(w.lower()): result.append(w)

        return result

    def isvalid(self, w):
        keymap = [
            set(list('qwertyuiop')),
            set(list('asdfghjkl')),
            set(list('zxcvbnm'))
        ]
        return True if any(map(lambda x: set(list(w)).issubset(x), keymap)) else False

