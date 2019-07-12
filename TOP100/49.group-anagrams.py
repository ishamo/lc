class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        if not strs: return result
        table = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in table: table[key] = []
            table[key].append(s)

        for v in table.values():
            result.append(list(v))

        return result




# 这。。。
# Actual
#   ✔ runtime: 24 ms
#   ✘ answer: [["bat"],["eat","tea","ate"],["tan","nat"]]
#   ✔ stdout: ''
#
# Expected
#   ✔ runtime: 0 ms
#   ✔ answer: [["bat"],["nat","tan"],["ate","eat","tea"]]
#   ✔ stdout: ''
