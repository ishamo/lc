# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        path = []
        def travel_for_path(root, pth):
            if not root: return
            p = pth[:]
            p.append(root.val)
            if not root.left and not root.right:
                path.append(p)
            else:
                if root.left:
                    travel_for_path(root.left, p)
                if root.right:
                    travel_for_path(root.right, p)

        travel_for_path(root, [])
        result = []
        # print('path', path)
        for p in path:
            val = reduce(lambda x, y: x+y, p)
            if val == sum:
                result.append(p)

        return result
#
#
# n1 = TreeNode(5)
# n2 = TreeNode(4)
# n3 = TreeNode(8)
# n4 = TreeNode(11)
# n5 = TreeNode(13)
# n6 = TreeNode(4)
# n7 = TreeNode(7)
# n8 = TreeNode(2)
# n9 = TreeNode(5)
# n10 = TreeNode(1)
#
# n1.left, n1.right = n2, n3
# n2.left = n4
# n3.left, n3.right = n5, n6
# n4.left, n4.right = n7, n8
# n6.left, n6.right = n9, n10
#
#
# s = Solution()
# print s.pathSum(n1, 22)
#
