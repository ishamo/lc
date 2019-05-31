# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        ret = []

        def inorder(root):
            if not root: return
            if root.left:
                inorder(root.left)
            ret.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)

        lenr = len(ret)
        for i in range(1, lenr):
            if ret[i] <= ret[i-1]: return False

        return True
