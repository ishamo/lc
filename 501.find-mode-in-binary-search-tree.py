# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root: return result

        self.inorder(root, result)

        table = {}
        for r in result:
            if r not in table:
                table[r] = 0
            table[r] += 1

        mx = max(table.values())
        ret = []
        for k, v in table.items():
            if v == mx: ret.append(k)

        return ret

    def inorder(self, root, result):
        if not root:
            return

        if root.left:
            self.inorder(root.left, result)

        result.append(root.val)

        if root.right:
            self.inorder(root.right, result)


