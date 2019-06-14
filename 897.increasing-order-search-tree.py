# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None

        result = []

        def inorder(root):
            if not root: return
            if root.left:
                inorder(root.left)
            result.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)

        if not result: return None

        head = TreeNode(result[0])
        p = head
        tail = None

        for item in result[1:]:
            tail = TreeNode(item)
            p.right = tail
            p = tail

        if tail:
            tail.right = None

        return head

