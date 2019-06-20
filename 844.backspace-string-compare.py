class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return True if self.dismiss(T) == self.dismiss(S) else False

    def dismiss(self, S):
        while True:
            olds = S
            S = S.lstrip('#')
            idx = S.find('#')
            if idx > 0:
                S = S[:idx-1] + S[idx+1:]

            if olds == S: break

        return S
