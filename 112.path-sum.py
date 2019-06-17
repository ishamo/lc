# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        paths = []
        self.travel_path(root, paths, [])
        for p in paths:
            if reduce(lambda a, b: a+b, p) == sum: return True

        return False

    def travel_path(self, root, paths, current):
        if not root: return

        current = current[:]
        current.append(root.val)
        if not root.left and not root.right:
            paths.append(current)
            return
        else:
            if root.left:
                self.travel_path(root.left, paths, current)
            if root.right:
                self.travel_path(root.right, paths, current)


