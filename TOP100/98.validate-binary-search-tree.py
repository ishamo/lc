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

        result = []
        if not root: return True
        self.inorder(root, result)
        for idx, item in enumerate(result[1:], 1):
            if not item > result[idx-1]: return False

        return True

    def inorder(self, root, result):
        if not root: return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
        
