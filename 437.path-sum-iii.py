# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = 0
        if not root: return count
        if root.left:
            count = count + self.pathSum(root.left, sum) + self.pathSum(root.left, sum-root.val)
        if root.right:
            count = count + self.pathSum(root.right, sum) + self.pathSum(root.right, sum-root.val)

        if sum == root.val:
            count += 1

        return count
