class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        newpath = path.replace('//', '/').replace('..', '*')
        while newpath != path:
            path = newpath
            newpath = newpath.replace('//', '/').replace('..', '*')

        path = path.strip('/')

        path = path.split('/')

        result = []
        for p in path:
            if p == '.':
                continue
            elif p == '*':
                if result:
                    result.pop(-1)
            else:
                result.append(p)

        ret = '/' + '/'.join(result)
        ret = ret.replace('*', '..')
        return ret
