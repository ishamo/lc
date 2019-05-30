class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        current = '1'
        for i in range(1, n):
            cnt = 0
            newstr = ''
            for idx, item in enumerate(current):
                if idx == 0:
                    cnt = 1
                    continue

                if current[idx] == current[idx-1]:
                    cnt += 1
                else:
                    newstr += str(cnt) + current[idx-1]
                    cnt = 1

            newstr += str(cnt) + current[-1]
            current = newstr
        return current
#
#
# s = Solution()
# for i in range(1, 6):
#     print s.countAndSay(i)
