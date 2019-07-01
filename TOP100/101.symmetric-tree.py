# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if self.theSame(root.left, root.right): return True
        return False

    def theSame(self, left, right):
        if not left and not right: return True
        elif left and not right or right and not left: return False
        else:
            if not left.val == right.val: return False
            return self.theSame(left.left, right.right) and self.theSame(left.right, right.left)
