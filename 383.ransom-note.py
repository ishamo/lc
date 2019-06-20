class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        A, B = {}, {}
        for m in magazine:
            if m not in B:
                B[m] = 0
            B[m] += 1

        for r in ransomNote:
            if r not in A:
                A[r] = 0
            A[r] += 1

        for k, v in A.items():
            if not k in B or B[k] < v: return False

        return True

