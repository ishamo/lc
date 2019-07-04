# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sm = 0
        return self.helper(root)

    def helper(self, root):
        if not root: return None

        if root.right:
            self.helper(root.right)

        self.sm += root.val
        root.val = self.sm

        if root.left:
            self.helper(root.left)

        return root


