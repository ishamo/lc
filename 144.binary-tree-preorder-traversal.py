# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        p = root
        ret = []
        stack = []
        while stack or p:
            while p:
                ret.append(p.val)
                stack.append(p)
                p = p.left
            top = stack.pop(-1)
            p = top.right
        return ret
#
#
# if __name__ == '__main__':
#
#     #     1
#     #  2     3
#     #    4  5
#
#     n1 = TreeNode(1)
#     n2 = TreeNode(2)
#     n3 = TreeNode(3)
#     n4 = TreeNode(4)
#     n5 = TreeNode(5)
#
#     n1.left = n2
#     n2.right = n4
#     n1.right = n3
#     n3.left = n5
#
#     s = Solution()
#     v = s.preorderTraversal(n1)
#     print v
