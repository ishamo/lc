class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1: return True
        len1 = len(s1)
        len2 = len(s2)
        if len1 > len2: return False

        S, V = [0]*26, [0]*26
        for i in range(len1):
            S[ord(s1[i])-ord('a')] += 1
            V[ord(s2[i])-ord('a')] += 1

        # print('S', S)
        for i in range(len1-1, len2):
            if S == V: return True
            if i == len1-1: continue
            else:
                V[ord(s2[i-len1])-ord('a')] -= 1
                V[ord(s2[i])-ord('a')] += 1
                # print('V', V)
                if S == V: return True

        return False


#
# s1 = "adc"
# s2 = "dcda"
# #
#
# s = Solution()
# print s.checkInclusion(s1, s2)
# print s1, s2
