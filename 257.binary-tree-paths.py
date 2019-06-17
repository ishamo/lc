# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        self.search_path(root, path, [])

        result = []
        for p in path:
            result.append('->'.join(p))

        return result

    def search_path(self, root, path, current):
        if not root: return
        current = current[:]
        current.append(str(root.val))
        if not root.left and not root.right:
            path.append(current)
            return
        else:
            if root.left:
                self.search_path(root.left, path, current)
            if root.right:
                self.search_path(root.right, path, current)
