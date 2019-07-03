# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.helper(root)

    def helper(self, root):
        if not root: return None
        tmp = self.helper(root.right)
        root.right = self.helper(root.left)
        root.left = None
        p = root
        while p.right:
            p = p.right

        p.right = tmp
        return root
