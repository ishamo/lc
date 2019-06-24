# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not t: return True
        if not s: return False

        if self.isSame(s, t): return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        # return False

    def isSame(self, one, other):
        if not one and not other: return True
        if one and other:
            if not one.val == other.val: return False
            return self.isSame(one.left, other.left) and self.isSame(one.right, other.right)
        else:
            return False

