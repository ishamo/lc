# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder: return None
        node = TreeNode(postorder[-1])
        idx = inorder.index(node.val)
        postorder.pop(-1)
        node.left = self.buildTree(inorder[0:idx], [i for i in postorder if i in inorder[0:idx]])
        node.right = self.buildTree(inorder[idx+1:], [i for i in postorder if i in inorder[idx+1:]])
        return node


# [9,3,15,20,7]
# [9,15,7,20,3]
