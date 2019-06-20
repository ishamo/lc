# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tilt, sm = self._findTilt(root)
        return tilt

    def _findTilt(self, root):
        if not root: return 0, 0

        if root.left and root.right:
            left_tilt, left_sm = self._findTilt(root.left)
            right_tilt, right_sm = self._findTilt(root.right)
            return left_tilt+right_tilt+abs(left_sm-right_sm), left_sm+right_sm+root.val
        elif root.left:
            left_tilt, left_sm = self._findTilt(root.left)
            return left_tilt+abs(left_sm), left_sm+root.val
        elif root.right:
            right_tilt, right_sm = self._findTilt(root.right)
            return right_tilt+abs(right_sm), right_sm+root.val
        else:
            return 0, root.val
