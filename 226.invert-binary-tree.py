# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
#
# n1 = TreeNode(4)
# n2 = TreeNode(2)
# n3 = TreeNode(7)
# n4 = TreeNode(1)
# n5 = TreeNode(3)
# n6 = TreeNode(6)
# n7 = TreeNode(9)
#
# n1.left, n1.right = n2, n3
# n2.left, n2.right = n4, n5
# n3.left, n3.right = n6, n7
#
#
# s = Solution()
# s.invertTree(n1)
