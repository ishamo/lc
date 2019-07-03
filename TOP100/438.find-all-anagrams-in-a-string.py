class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        result = []
        if not s or not p: return result

        template = {}
        for i in p:
            if i not in template:
                template[i] = 0
            template[i] += 1

        origin = {}
        for idx, c in enumerate(s[0:len(s)]):
            if c not in origin:
                origin[c] = 0
            origin[c] += 1
            if idx >= len(p):
                origin[s[idx-len(p)]] -= 1

            if self.isSame(template, origin): result.append(idx+1-len(p))
        return result

    def isSame(self, template, origin):
        # print('template, origin', template, origin)
        for key in template:
            if key not in origin or origin[key] != template[key]: return False
        return True
        
# s = "abacbabc"
# p = "abc"
# S = Solution()
# print S.findAnagrams(s, p)
# print 's', 'p', s, p
