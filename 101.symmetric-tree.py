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
        if not root or not root.left and not root.right: return True

        new_tree = self.buildTree(root)

        return self.sameTree(root, new_tree)

    def buildTree(self, root):
        if not root: return None
        new_tree = TreeNode(root.val)
        new_tree.left = self.buildTree(root.right)
        new_tree.right = self.buildTree(root.left)
        return new_tree

    def sameTree(self, root, new_tree):
        if not root and not new_tree: return True
        if not root and new_tree or root and not new_tree: return False

        if not root.val == new_tree.val: return False

        return self.sameTree(root.left, new_tree.left) and self.sameTree(root.right, new_tree.right)
