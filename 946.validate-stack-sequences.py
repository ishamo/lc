class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        len1, len2 = len(pushed), len(popped)
        if not len1 == len2: return False
        i = len1-1
        j = 0
        stack = []
        while True:

            if stack and stack[-1] == pushed[i]:
                stack.pop(-1)
                i -= 1

            else:
                if j >= len2: break
                stack.append(popped[j])
                j += 1

            print('stack', stack, 'i, j', i, j)

        if stack: return False

        return True


s = Solution()
# pushed = [1,2,3,4,5]
# popped = [4,5,3,2,1]
pushed = [1,0,2]
popped = [2,1,0]
print s.validateStackSequences(pushed, popped)



