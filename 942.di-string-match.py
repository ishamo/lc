class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        if not S: return result

        mn, mx = 0, len(S)

        for i in range(len(S)):
            if S[i] == 'D':
                result.append(mx)
                mx -= 1
            else:
                result.append(mn)
                mn += 1

        result.append(mn)
        return result


