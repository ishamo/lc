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
        if not root: return root

        if root.right:
            self.convertBST(root.right)
            root.val += root.right.val

        if root.left:
            self.convertBST(root.left)
            root.left.val += root.val

        return root
