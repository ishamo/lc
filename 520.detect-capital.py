class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        lenw = len(word)

        if lenw == 1: return True

        if 'a' <= word[0] <= 'z':
            for i in range(1, lenw):
                if not 'a'<=word[i]<='z': return False

        if 'A' <= word[0] <= 'Z':
            if 'A' <= word[1] <= 'Z':
                for i in range(2, lenw):
                    if not 'A' <= word[i] <= 'Z': return False

            if 'a' <= word[1] <= 'z':
                for i in range(2, lenw):
                    if not 'a' <= word[i] <= 'z': return False

        return True


