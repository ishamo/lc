# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p: return True
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
#
#
# if __name__ == '__main__':
#     n1 = TreeNode(1)
#     n2 = TreeNode(2)
#     n3 = TreeNode(3)
#     n4 = TreeNode(4)
#     n5 = TreeNode(5)
#     n1.left, n1.right = n2, n3
#     n2.left = n4
#     n3.right = n5
#
#     s = Solution()
#     print(s.isSameTree(n1, n1))
#     print(s.isSameTree(n1, n2))
