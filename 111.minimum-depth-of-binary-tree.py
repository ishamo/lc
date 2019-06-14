# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0

        # 不要算0就行了
        lvalue = self.minDepth(root.left)
        rvalue = self.minDepth(root.right)

        if lvalue and rvalue:
            return 1 + min(lvalue, rvalue)
        elif lvalue:
            return 1 + lvalue
        elif rvalue:
            return 1 + rvalue
        else:
            return 1
