# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        cnt = [0]
        self.do_the_cnt(root, cnt)

        return cnt[0]

    def do_the_cnt(self, root, cnt):
        cnt[0] += 1
        if root.left:
            self.do_the_cnt(root.left, cnt)
        if root.right:
            self.do_the_cnt(root.right, cnt)
