# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        path = self.enumAllPath(root)

        return sum([int(item) for item in path])

    def enumAllPath(self, root):
        path = []
        self.helper(root, path)
        return path

    def helper(self, root, path, current=''):
        if not root: return
        current += str(root.val)
        if not root.left and not root.right:
            path.append(current)
        if root.left:
            self.helper(root.left, path, current)
        if root.right:
            self.helper(root.right, path, current)
        return
